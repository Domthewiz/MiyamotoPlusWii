# Unused Wii Actors
# Custom Miyamoto sprites.py Module
# Sprites Images

import math

from PyQt5 import QtCore, QtGui
from PyQt5.QtCore import *
from PyQt5.QtGui import *

Qt = QtCore.Qt

import spritelib as SLib

ImageCache = SLib.ImageCache

# Global varible for rotations.
Rotations = [0, 0, 0]
StoneRotation = 0

class SpriteImage_ActorSpawner(SLib.SpriteImage_Static):  # 724
    def __init__(self, parent):
        super().__init__(
            parent,
            3.75,
            ImageCache['actor'],
            (0, 0),
        )

    def loadImages():
        SLib.loadIfNotInImageCache('actor', 'Actor_Spawner.png')


class SpriteImage_MassiveSpikedStake(SLib.SpriteImage_Static):  # 377
    def __init__(self, parent):
        super().__init__(
            parent,
            3.75,
            ImageCache['MassiveSpikedStake'],
            (-98, -2445),
        )

    def loadImages():
        SLib.loadIfNotInImageCache('MassiveSpikedStake', 'massive_stake_down_e_0.png')


class SpriteImage_MortyMole(SLib.SpriteImage_Static):  # 692
    def __init__(self, parent):
        super().__init__(
            parent,
            3.75,
            ImageCache['mortymole'],
            (0, 0),
        )

    def loadImages():
        SLib.loadIfNotInImageCache('mortymole', 'mortymole.png')


class SpriteImage_Parabones(SLib.SpriteImage_Static):  # 725
    def __init__(self, parent):
        super().__init__(
            parent,
            3.75,
            ImageCache['Parabones'],
            (0, -6),
        )

    def loadImages():
        SLib.loadIfNotInImageCache('Parabones', 'Parabones.png')

   
class SpriteImage_Cataquack(SLib.SpriteImage_Static):  # 733
    def __init__(self, parent):
        super().__init__(
            parent,
            3.75,
            ImageCache['Cataquack'],
            (-10, -19),
        )

    def loadImages():
        SLib.loadIfNotInImageCache('Cataquack', 'cataquack.png')


class SpriteImage_RainbowLight(SLib.SpriteImage_Static):  # 738
    def __init__(self, parent):
        super().__init__(
            parent,
            3.75,
            ImageCache['RainbowLight'],
            (0, 0),
        )

    def loadImages():
        SLib.loadIfNotInImageCache('RainbowLight', 'light.png')


class SpriteImage_CustomDoor(SLib.SpriteImage_Static):  # 726
    def __init__(self, parent):
        super().__init__(
            parent,
            3.75,
            ImageCache['CustomDoor'],
            (-16, -16),
        )

    @staticmethod
    def loadImages():
        SLib.loadIfNotInImageCache('CustomDoor', 'customdoor.png')


class SpriteImage_TimeClock(SLib.SpriteImage_Static):  # 734
    def __init__(self, parent):
        super().__init__(
            parent,
            3.75,
            ImageCache['TimeClock'],
            (-16, -16),
        )

    @staticmethod
    def loadImages():
        SLib.loadIfNotInImageCache('TimeClock', 'time_clock.png')

class SpriteImage_FakeActor(SLib.SpriteImage_Static):  # 727
    def __init__(self, parent):
        super().__init__(
            parent,
            3.75,
        )

    @staticmethod
    def loadImages():
        SLib.loadIfNotInImageCache('fake_midway', 'fake_midwayflag.png')
        SLib.loadIfNotInImageCache('fake_goalpoal', 'fake_goalpoal.png')
        SLib.loadIfNotInImageCache('fake_starcoin', 'fake_starcoin.png')
          
    def dataChanged(self):
        style = self.parent.spritedata[5] & 0xF
         
        if style == 1:
            self.image = ImageCache['fake_goalpoal']

            self.xOffset = -36
            self.yOffset = -160

        elif style == 2:
            self.image = ImageCache['fake_starcoin']

            self.xOffset = -16
            self.yOffset = -16
        else:
            self.image = ImageCache['fake_midway']

            self.xOffset = -8
            self.yOffset = -56
            

        super().dataChanged()

        
class SpriteImage_Scuttlebug(SLib.SpriteImage_Static):  # 749
    def __init__(self, parent):
        super().__init__(
            parent,
            3.75,
            ImageCache['scuttlebug'],
            (0, 0),
        )

    def loadImages():
        SLib.loadIfNotInImageCache('scuttlebug', 'scuttlebug.png')
    
class SpriteImage_Biddybud(SLib.SpriteImage_Static):  # 758
    def __init__(self, parent):
        super().__init__(
            parent,
            3.75,
            ImageCache['Biddybud'],
            (-8, 0),
        )

    def loadImages():
        SLib.loadIfNotInImageCache('Biddybud', 'biddybud_red.png')
        
class SpriteImage_BasaltBones(SLib.SpriteImage_Static):  # 760
    def __init__(self, parent):
        super().__init__(
            parent,
            3.75,
            ImageCache['BasaltBones'],
            (-32, -40),
        )

    def loadImages():
        SLib.loadIfNotInImageCache('BasaltBones', 'basaltbones.png')
        
class SpriteImage_TripleBlock(SLib.SpriteImage_Static):  # 766
    def __init__(self, parent):
        super().__init__(
            parent,
            3.75,
        )

        self.xOffset = -16
        self.yOffset = -16

    @staticmethod
    def loadImages():
        SLib.loadIfNotInImageCache('TripleBlock_standard', 'triple_block_standard.png')
        SLib.loadIfNotInImageCache('TripleBlock_chika', 'triple_block_chika.png')
        SLib.loadIfNotInImageCache('TripleBlock_yougan', 'triple_block_yougan.png')
        SLib.loadIfNotInImageCache('TripleBlock_yougan2', 'triple_block_yougan2.png')
          
    def dataChanged(self):
        animationStyle = self.parent.spritedata[0] & 0xF
            
        if animationStyle == 1:
            self.image = ImageCache['TripleBlock_chika']

        elif animationStyle == 2:
            self.image = ImageCache['TripleBlock_yougan']

        elif animationStyle == 3:
            self.image = ImageCache['TripleBlock_yougan2']
    
        else:
            self.image = ImageCache['TripleBlock_standard']

        super().dataChanged()


class SpriteImage_Peepa(SLib.SpriteImage_StaticMultiple):  # 770 TODO: add different platform variations?
    def __init__(self, parent):
        super().__init__(
            parent,
            3.75,
        )

        self.xOffset = 0

    @staticmethod
    def loadImages():
        SLib.loadIfNotInImageCache('PeepaWoodPlat', 'peepa_platform.png')
        SLib.loadIfNotInImageCache('Peepa', 'peepa.png')
          
    def dataChanged(self):
        has_platform = (self.parent.spritedata[0] >> 1) & 8       
        
        if has_platform == 0:
            self.image = ImageCache['Peepa']
            
        elif has_platform == 8:
            self.image = ImageCache['PeepaWoodPlat']
            self.xOffset = -24
            

        super().dataChanged()


class SpriteImage_StarCoinShard(SLib.SpriteImage_Static):  # 729
    def __init__(self, parent):
        super().__init__(
            parent,
            3.75,
            ImageCache['StarCoinShard'],
            (-8, -8),
        )

    def loadImages():
        SLib.loadIfNotInImageCache('StarCoinShard', 'star_coin_shard.png')
        
class SpriteImage_Kamiya(SLib.SpriteImage_Static):  # 743
    def __init__(self, parent):
        super().__init__(
            parent,
            3.75,
            ImageCache['Kamiya'],
            (-24, -32),
        )

    def loadImages():
        SLib.loadIfNotInImageCache('Kamiya', 'kamiya.png')

class SpriteImage_BeepBlock(SLib.SpriteImage_Static):  # 730
    def __init__(self, parent):
        super().__init__(
            parent,
            3.75,
        )

    @staticmethod
    def loadImages():
        SLib.loadIfNotInImageCache('beep_block_red', 'beep_block_red.png')
        SLib.loadIfNotInImageCache('beep_block_blue', 'beep_block_blue.png')
          
    def dataChanged(self):
        animationStyle = (self.parent.spritedata[0] >> 1) & 8
        
        if animationStyle == 8:
            self.image = ImageCache['beep_block_blue']
            
        else:
             self.image = ImageCache['beep_block_red']
            

        super().dataChanged()
        
             
class SpriteImage_Chestnut(SLib.SpriteImage_Static):  # 731
    def __init__(self, parent):
        super().__init__(
            parent,
            3.75,
            ImageCache['Chestnut'],
            (-8, -8),
        )

    def loadImages():
        SLib.loadIfNotInImageCache('Chestnut', 'chestnut.png')
        
class SpriteImage_Flaptor(SLib.SpriteImage_Static):  # 761
    def __init__(self, parent):
        super().__init__(
            parent,
            3.75,
            ImageCache['Flaptor'],
            (-16, -8),
        )

    def loadImages():
        SLib.loadIfNotInImageCache('Flaptor', 'flaptor.png')
        
class SpriteImage_ColdFuzzy(SLib.SpriteImage_Static):  # 753
    def __init__(self, parent):
        super().__init__(
            parent,
            3.75,
            ImageCache['ColdFuzzy'],
            (-16, -16),
        )

    def loadImages():
        SLib.loadIfNotInImageCache('ColdFuzzy', 'coldfuzzy.png')

       


class SpriteImage_ActrSpawner(SLib.SpriteImage_Static):  # 724
    def __init__(self, parent):
        super().__init__(
            parent,
            3.75,
            ImageCache['acor'],
            (0, -240),
        )

    def loadImages():
        SLib.loadIfNotInImageCache('acor', 'Actr_Spawner.png')
class SpriteImage_TiltGirder(SLib.SpriteImage_Static):  # 724
    def __init__(self, parent):
        super().__init__(
            parent,
            3.75,
            ImageCache['girder'],
            (0, -16.7),
        )

    def loadImages():
        SLib.loadIfNotInImageCache('girder', 'tilt_girder.png')
        

class SpriteImage_LightGem(SLib.SpriteImage_Static):  # 724
    def __init__(self, parent):
        super().__init__(
            parent,
            3.75,
            ImageCache['lightgem'],
            (0, 0),
        )

    def loadImages():
        SLib.loadIfNotInImageCache('lightgem', 'light_gem.png')

class SpriteImage_CubeM(SLib.SpriteImage_StaticMultiple):  # 539
    def __init__(self, parent):
        super().__init__(
            parent,
            3.75,
        )
        
        self.parent.setZValue(-40000)

    @staticmethod
    def loadImages():
        SLib.loadIfNotInImageCache('cubem', 'cube_kinoko_M.png')

    def dataChanged(self):

        width = (self.parent.spritedata[8] & 0xF) + 1
        height = (self.parent.spritedata[9] & 0xF) + 1

        self.image = ImageCache['cubem'].scaled(width * 60, height * 60)
        self.yOffset = 0
            
        super().dataChanged()

class SpriteImage_ColoredBlock(SLib.SpriteImage_PivotRotationControlled):  # 539
    def __init__(self, parent):
        super().__init__(
            parent,
            3.75,
        )

    @staticmethod
    def loadImages():
        SLib.loadIfNotInImageCache('cbred', 'cbred.png')
        SLib.loadIfNotInImageCache('cbblue', 'cbblue.png')
        SLib.loadIfNotInImageCache('cbgreen', 'cbgreen.png')
        SLib.loadIfNotInImageCache('cbyellow', 'cbyellow.png')

    def dataChanged(self):

        self.affectImage = (self.parent.spritedata[3] & 1) != 1
        self.affectAUXImage = (self.parent.spritedata[3] & 1) != 1

        width = (self.parent.spritedata[8] & 0x1F) + 3
        height = (self.parent.spritedata[9] & 0x0F) + 3
        style = self.parent.spritedata[3] >> 4 & 0xF
         
        if style == 0:
            self.image = ImageCache['cbred'].scaled(width * 60, height * 60)
            self.yOffset = 0
            
        elif style == 1:
            self.image = ImageCache['cbblue'].scaled(width * 60, height * 60)
            self.yOffset = 0

        elif style == 2:
            self.image = ImageCache['cbgreen'].scaled(width * 60, height * 60)
            self.yOffset = 0

        else:
            self.image = ImageCache['cbyellow'].scaled(width * 60, height * 60)
            self.yOffset = 0
         
        super().dataChanged()


class SpriteImage_PropellerBlock(SLib.SpriteImage_Static):  # 724
    def __init__(self, parent):
        super().__init__(
            parent,
            3.75,
            ImageCache['blockflye'],
            (-1.866, -6.13),
        )

    def loadImages():
        SLib.loadIfNotInImageCache('blockflye', 'block_fly.png')
        
class SpriteImage_GlwBlock(SLib.SpriteImage_Static):  # 724
    def __init__(self, parent):
        super().__init__(
            parent,
            3.75,
            ImageCache['blockglowe'],
            (0, 0),
        )

    def loadImages():
        SLib.loadIfNotInImageCache('blockglowe', 'glow_block.png')

class SpriteImage_Crowber(SLib.SpriteImage_Static):  # 724
    def __init__(self, parent):
        super().__init__(
            parent,
            3.75,
            ImageCache['crowbere'],
            (-8, -2),
        )

    def loadImages():
        SLib.loadIfNotInImageCache('crowbere', 'crowber.png')
        
class SpriteImage_KoopaCave(SLib.SpriteImage_Static):  # 724
    def __init__(self, parent):
        super().__init__(
            parent,
            3.75,
            ImageCache['koopac'],
            (-112, -160),
        )

        self.parent.setZValue(-40000)

    def loadImages():
        SLib.loadIfNotInImageCache('koopac', 'koopa_cave.png')

class SpriteImage_LakituBlock(SLib.SpriteImage_Static):  # 724
    def __init__(self, parent):
        super().__init__(
            parent,
            3.75,
            ImageCache['lakbloc'],
            (-4, -8),
        )

    def loadImages():
        SLib.loadIfNotInImageCache('lakbloc', 'block_cloud.png')
        
class SpriteImage_SmallCannon(SLib.SpriteImage_Static):  # 724
    def __init__(self, parent):
        super().__init__(
            parent,
            3.75,
        )

    def loadImages():
        SLib.loadIfNotInImageCache('smallc', 'small_cannon.png')
        SLib.loadIfNotInImageCache('smallc_s', 'small_cannon_s.png')
        SLib.loadIfNotInImageCache('smallc_u', 'small_cannon_u.png')
        SLib.loadIfNotInImageCache('smallc_s_u', 'small_cannon_s_u.png')
        
    def dataChanged(self):
        style = self.parent.spritedata[5] & 0xF
        direction = self.parent.spritedata[5] >> 4 & 0xF
         
        if style == 0 and direction == 0:
            self.image = ImageCache['smallc_s']

            self.xOffset = -16
            self.yOffset = -32
            
        elif style == 1 and direction == 0:
            self.image = ImageCache['smallc']

            self.xOffset = -16
            self.yOffset = -32 

        elif style == 0 and direction == 1:
            self.image = ImageCache['smallc_s_u']

            self.xOffset = -16
            self.yOffset = 0   

        else:
            self.image = ImageCache['smallc_u']

            self.xOffset = -16
            self.yOffset = 0
         
        super().dataChanged()
        
        
class SpriteImage_BigCannon(SLib.SpriteImage_Static):  # 724
    def __init__(self, parent):
        super().__init__(
            parent,
            3.75,
        )

    def loadImages():
        SLib.loadIfNotInImageCache('bigc', 'big_cannon.png')
        SLib.loadIfNotInImageCache('bigc_s', 'big_cannon_s.png')
        SLib.loadIfNotInImageCache('bigc_s_u', 'big_cannon_s_u.png')
        SLib.loadIfNotInImageCache('bigc_u', 'big_cannon_u.png')
        
    def dataChanged(self):
        style = self.parent.spritedata[5] & 0xF
        direction = self.parent.spritedata[5] >> 4 & 0xF
         
        if style == 0 and direction == 0:
            self.image = ImageCache['bigc_s']

            self.xOffset = -40
            self.yOffset = -80
            
        elif style == 1 and direction == 0:
            self.image = ImageCache['bigc']

            self.xOffset = -40
            self.yOffset = -80 

        elif style == 0 and direction == 1:
            self.image = ImageCache['bigc_s_u']

            self.xOffset = -40
            self.yOffset = 0   

        else:
            self.image = ImageCache['bigc_u']

            self.xOffset = -40
            self.yOffset = 0
         
        super().dataChanged()
        
class SpriteImage_Metealbox(SLib.SpriteImage_Static):  # 724
    def __init__(self, parent):
        super().__init__(
            parent,
            3.75,
        )

    def loadImages():
        SLib.loadIfNotInImageCache('teeny', 'teeny_lift.png')
        SLib.loadIfNotInImageCache('small', 'small_lift.png')
        SLib.loadIfNotInImageCache('big', 'big_lift.png')
        
    def dataChanged(self):
        style = self.parent.spritedata[8] & 0xF
         
        if style == 0:
            self.image = ImageCache['teeny']

            self.xOffset = 0
            self.yOffset = 0   
            
        elif style == 1:
            self.image = ImageCache['small']

            self.xOffset = 0
            self.yOffset = 0   

        else:
            self.image = ImageCache['big']

            self.xOffset = 0
            self.yOffset = 0
         
        super().dataChanged()
        
class SpriteImage_LiftTaru(SLib.SpriteImage_Static):  # 724
    def __init__(self, parent):
        super().__init__(
            parent,
            3.75,
            ImageCache['tarue'],
            (-16, 0),
        )

    def loadImages():
        SLib.loadIfNotInImageCache('tarue', 'lift_taru.png')
        SLib.loadIfNotInImageCache('tarul', 'lift_taru_large.png')
        
    def dataChanged(self):
        style = self.parent.spritedata[5] & 0xF
         
        if style == 0:
            self.image = ImageCache['tarue']

            self.xOffset = -16
            self.yOffset = 0   

        else:
            self.image = ImageCache['tarul']

            self.xOffset = -40
            self.yOffset = -24
            

        super().dataChanged()

class SpriteImage_Kumiawase(SLib.SpriteImage_Static):  # 727
    def __init__(self, parent):
        super().__init__(
            parent,
            3.75,
        )

    @staticmethod
    def loadImages():
        SLib.loadIfNotInImageCache('2x2', '2x2.png')
        SLib.loadIfNotInImageCache('2x3', '3x2.png')
        SLib.loadIfNotInImageCache('3x2', '2x3.png')
        SLib.loadIfNotInImageCache('3x3', '3x3.png')
        SLib.loadIfNotInImageCache('2x4', '2x4.png')
        SLib.loadIfNotInImageCache('4x4', '4x4.png')
        SLib.loadIfNotInImageCache('2x6', '2x6.png')
          
    def dataChanged(self):
        style = self.parent.spritedata[5] & 0xF
         
        if style == 0:
            self.image = ImageCache['2x2']

            self.xOffset = 0
            self.yOffset = 0

        elif style == 1:
            self.image = ImageCache['2x3']

            self.xOffset = 0
            self.yOffset = 0
        
        elif style == 2:
            self.image = ImageCache['3x2']

            self.xOffset = 0
            self.yOffset = 0
        
        elif style == 3:
            self.image = ImageCache['3x3']

            self.xOffset = 0
            self.yOffset = 0
        
        elif style == 4:
            self.image = ImageCache['2x4']

            self.xOffset = 0
            self.yOffset = 0
        
        elif style == 5:
            self.image = ImageCache['4x4']

            self.xOffset = 0
            self.yOffset = 0
        else:
            self.image = ImageCache['2x6']

            self.xOffset = 0
            self.yOffset = 0
            

        super().dataChanged()


class SpriteImage_FakActor(SLib.SpriteImage_Static):  # 727
    def __init__(self, parent):
        super().__init__(
            parent,
            3.75,
        )

    @staticmethod
    def loadImages():
        SLib.loadIfNotInImageCache('w0', 'w0.png')
        SLib.loadIfNotInImageCache('w1', 'w1.png')
        SLib.loadIfNotInImageCache('w2', 'w2.png')
        SLib.loadIfNotInImageCache('w3', 'w3.png')
        SLib.loadIfNotInImageCache('w4', 'w4.png')
        SLib.loadIfNotInImageCache('w5', 'w5.png')
        SLib.loadIfNotInImageCache('w6', 'w6.png')
        SLib.loadIfNotInImageCache('w7', 'w7.png')
        SLib.loadIfNotInImageCache('w8', 'w8.png')
        SLib.loadIfNotInImageCache('w9', 'w9.png')
        SLib.loadIfNotInImageCache('wa', 'wa.png')
        SLib.loadIfNotInImageCache('wb', 'wb.png')
        SLib.loadIfNotInImageCache('wc', 'wc.png')
        SLib.loadIfNotInImageCache('wd', 'wd.png')
        SLib.loadIfNotInImageCache('we', 'we.png')
        SLib.loadIfNotInImageCache('wf', 'wf.png')
          
    def dataChanged(self):
        style = self.parent.spritedata[8] & 0xF
         
        if style == 0:
            self.image = ImageCache['w0']

            self.xOffset = 0
            self.yOffset = 0

        elif style == 1:
            self.image = ImageCache['w1']

            self.xOffset = 0
            self.yOffset = 0
        
        elif style == 2:
            self.image = ImageCache['w2']

            self.xOffset = 0
            self.yOffset = 0
        
        elif style == 3:
            self.image = ImageCache['w3']

            self.xOffset = 0
            self.yOffset = 0
        
        elif style == 4:
            self.image = ImageCache['w4']

            self.xOffset = 0
            self.yOffset = 0
        
        elif style == 5:
            self.image = ImageCache['w5']

            self.xOffset = 0
            self.yOffset = 0
        
        elif style == 6:
            self.image = ImageCache['w6']

            self.xOffset = 0
            self.yOffset = 0
        
        elif style == 7:
            self.image = ImageCache['w7']

            self.xOffset = 0
            self.yOffset = 0
        
        elif style == 8:
            self.image = ImageCache['w8']

            self.xOffset = 0
            self.yOffset = 0
        
        elif style == 9:
            self.image = ImageCache['w9']

            self.xOffset = 0
            self.yOffset = 0
        
        elif style == 10:
            self.image = ImageCache['wa']

            self.xOffset = 0
            self.yOffset = 0
        elif style == 11:
            self.image = ImageCache['wb']

            self.xOffset = 0
            self.yOffset = 0
        
        elif style == 12:
            self.image = ImageCache['wc']

            self.xOffset = 0
            self.yOffset = 0
        
        elif style == 13:
            self.image = ImageCache['wd']

            self.xOffset = 0
            self.yOffset = 0
        
        elif style == 14:
            self.image = ImageCache['we']

            self.xOffset = 0
            self.yOffset = 0
        
        else:
            self.image = ImageCache['wf']

            self.xOffset = 0
            self.yOffset = 0
            

        super().dataChanged()

class SpriteImage_RotoDisc(SLib.SpriteImage_PivotRotationControlled):  # 96
    affectImage = affectAUXImage = False
    def __init__(self, parent):
        super().__init__(
            parent,
            3.75,
        )
        
        self.aux.append(SLib.AuxiliaryImage(parent, 1, 1))

    @staticmethod
    def loadImages():
        SLib.loadIfNotInImageCache('roto_disc_small', 'roto_disc_small.png')
        SLib.loadIfNotInImageCache('roto_disc_large', 'roto_disc_large.png')

    def dataChanged(self):

        self.affectImage = 1 != 1

        if self.parent.spritedata[2] >> 4 & 1:
            self.dimensions = (-8, -16, 32, 32)
            self.aux[0].setImage(ImageCache['roto_disc_large'], 0, 0)

        else:
            self.dimensions = (0, 0, 16, 16)
            self.aux[0].setImage(ImageCache['roto_disc_small'], 0, 0)

        super().dataChanged()

class SpriteImage_MushroomCube(SLib.SpriteImage_PivotRotationControlled):  # 96
    def __init__(self, parent):
        super().__init__(
            parent,
            3.75,
        )
        
        self.aux.append(SLib.AuxiliaryImage(parent, 1, 1))

    @staticmethod
    def loadImages():
        SLib.loadIfNotInImageCache('mushsmall', 'cube_kinoko_S.png')
        SLib.loadIfNotInImageCache('mushbig', 'cube_kinoko_L.png')

    def dataChanged(self):
        
        self.affectImage = (self.parent.spritedata[3] & 1) != 1
        self.affectAUXImage = (self.parent.spritedata[3] & 1) != 1

        if self.parent.spritedata[4] & 1:
            self.dimensions = (0, 0, 240, 240)
            self.aux[0].setImage(ImageCache['mushbig'], 0, 0)

        else:
            self.dimensions = (0, 0, 80, 80)
            self.aux[0].setImage(ImageCache['mushsmall'], 0, 0)

        super().dataChanged()

class SpriteImage_PipeBubbles(SLib.SpriteImage_PivotRotationControlled):  # 263
    def __init__(self, parent):
        super().__init__(
            parent,
            3.75,
        )
        self.parent.setZValue(-40000)
        self.aux.append(SLib.AuxiliaryImage(parent, 1, 1))

    @staticmethod
    def loadImages():
        SLib.loadIfNotInImageCache('PipeBubbles0', 'pipe_bubbles.png')
        SLib.loadIfNotInImageCache('PipeBubbles1', 'pipe_bubbles_d.png')
        SLib.loadIfNotInImageCache('PipeBubbles2', 'pipe_bubbles_r.png')
        SLib.loadIfNotInImageCache('PipeBubbles3', 'pipe_bubbles_l.png')
        
    def dataChanged(self):
        direction = self.parent.spritedata[5] & 3
        self.image = ImageCache['PipeBubbles%d' % direction]

        if direction == 1:
            self.offset = (0, 16)
        elif direction == 2:
            self.offset = (16, -16)
        elif direction == 3:
            self.offset = (-96, -16)
        else:
            self.offset = (0, -96)
        
        super().dataChanged()

class SpriteImage_PivotalIronBlock(SLib.SpriteImage_PivotRotationControlled):  # 434
    def __init__(self, parent):
        super().__init__(
            parent,
            3.75,
        )

    @staticmethod
    def loadImages():
        SLib.loadIfNotInImageCache('1GhostShipBlockT', 'mov_iron_top_m.png')
        SLib.loadIfNotInImageCache('1GhostShipBlockTL', 'mov_iron_top_l.png')
        SLib.loadIfNotInImageCache('1GhostShipBlockTR', 'mov_iron_top_r.png')
        SLib.loadIfNotInImageCache('1GhostShipBlockL', 'mov_iron_middle_l.png')
        SLib.loadIfNotInImageCache('1GhostShipBlockM', 'mov_iron_middle_m.png')
        SLib.loadIfNotInImageCache('1GhostShipBlockR', 'mov_iron_middle_r.png')
        SLib.loadIfNotInImageCache('1GhostShipBlockB', 'mov_iron_bottom_m.png')
        SLib.loadIfNotInImageCache('1GhostShipBlockBL', 'mov_iron_bottom_l.png')
        SLib.loadIfNotInImageCache('1GhostShipBlockBR', 'mov_iron_bottom_r.png')

    def dataChanged(self):

        self.affectImage = (self.parent.spritedata[3] & 1) != 1
        self.affectAUXImage = (self.parent.spritedata[3] & 1) != 1

        self.w = (self.parent.spritedata[8] & 0x1F) + 3
        self.h = (self.parent.spritedata[9] & 0x0F) + 3
        self.width = self.w << 4
        self.height = self.h << 4

        pix = QtGui.QPixmap(self.width * 3.75, self.height * 3.75)
        pix.fill(Qt.transparent)

        painter = QtGui.QPainter(pix)

        # Draw middle
        painter.drawTiledPixmap(60, 60, (self.w - 2) * 60, (self.h - 2) * 60, ImageCache['1GhostShipBlockM'], 15, ImageCache['1GhostShipBlockM'].height() - (((self.h - 2) * 60) % ImageCache['1GhostShipBlockM'].height()))

        # Draw top row
        painter.drawPixmap(0, 0, ImageCache['1GhostShipBlockTL'])
        painter.drawTiledPixmap(60, 0, (self.w - 2) * 60, 60, ImageCache['1GhostShipBlockT'])
        painter.drawPixmap((self.w - 1) * 60, 0, ImageCache['1GhostShipBlockTR'])

        # Draw left and right side
        painter.drawTiledPixmap(0, 60, 60, (self.h - 2) * 60, ImageCache['1GhostShipBlockL'])
        painter.drawTiledPixmap((self.w - 1) * 60, 60, 60, (self.h - 2) * 60, ImageCache['1GhostShipBlockR'])

        # Draw bottom row
        painter.drawPixmap(0, (self.h - 1) * 60, ImageCache['1GhostShipBlockBL'])
        painter.drawTiledPixmap(60, (self.h - 1) * 60, (self.w - 2) * 60, 60, ImageCache['1GhostShipBlockB'])
        painter.drawPixmap((self.w - 1) * 60, (self.h - 1) * 60, ImageCache['1GhostShipBlockBR'])

        painter.end()
        del painter

        self.image = pix

        super().dataChanged()

class SpriteImage_GhostShipBlock(SLib.SpriteImage_PivotRotationControlled):  # 512
    def __init__(self, parent):
        super().__init__(
            parent,
            3.75,
        )

    @staticmethod
    def loadImages():
        SLib.loadIfNotInImageCache('GhostShipBlockT', 'ghost_ship_block_t.png')
        SLib.loadIfNotInImageCache('GhostShipBlockTL', 'ghost_ship_block_tl.png')
        SLib.loadIfNotInImageCache('GhostShipBlockTR', 'ghost_ship_block_tr.png')
        SLib.loadIfNotInImageCache('GhostShipBlockL', 'ghost_ship_block_l.png')
        SLib.loadIfNotInImageCache('GhostShipBlockM', 'ghost_ship_block_m.png')
        SLib.loadIfNotInImageCache('GhostShipBlockR', 'ghost_ship_block_r.png')
        SLib.loadIfNotInImageCache('GhostShipBlockB', 'ghost_ship_block_b.png')
        SLib.loadIfNotInImageCache('GhostShipBlockBL', 'ghost_ship_block_bl.png')
        SLib.loadIfNotInImageCache('GhostShipBlockBR', 'ghost_ship_block_br.png')

    def dataChanged(self):

        self.affectImage = (self.parent.spritedata[3] & 1) != 1
        self.affectAUXImage = (self.parent.spritedata[3] & 1) != 1

        self.w = (self.parent.spritedata[8] & 0x1F) + 3
        self.h = (self.parent.spritedata[9] & 0x0F) + 3
        self.width = self.w << 4
        self.height = self.h << 4

        pix = QtGui.QPixmap(self.width * 3.75, self.height * 3.75)
        pix.fill(Qt.transparent)

        painter = QtGui.QPainter(pix)

        # Draw middle
        painter.drawTiledPixmap(60, 60, (self.w - 2) * 60, (self.h - 2) * 60, ImageCache['GhostShipBlockM'], 15, ImageCache['GhostShipBlockM'].height() - (((self.h - 2) * 60) % ImageCache['GhostShipBlockM'].height()))

        # Draw top row
        painter.drawPixmap(0, 0, ImageCache['GhostShipBlockTL'])
        painter.drawTiledPixmap(60, 0, (self.w - 2) * 60, 60, ImageCache['GhostShipBlockT'])
        painter.drawPixmap((self.w - 1) * 60, 0, ImageCache['GhostShipBlockTR'])

        # Draw left and right side
        painter.drawTiledPixmap(0, 60, 60, (self.h - 2) * 60, ImageCache['GhostShipBlockL'])
        painter.drawTiledPixmap((self.w - 1) * 60, 60, 60, (self.h - 2) * 60, ImageCache['GhostShipBlockR'])

        # Draw bottom row
        painter.drawPixmap(0, (self.h - 1) * 60, ImageCache['GhostShipBlockBL'])
        painter.drawTiledPixmap(60, (self.h - 1) * 60, (self.w - 2) * 60, 60, ImageCache['GhostShipBlockB'])
        painter.drawPixmap((self.w - 1) * 60, (self.h - 1) * 60, ImageCache['GhostShipBlockBR'])

        painter.end()
        del painter

        self.image = pix

        super().dataChanged()

class SpriteImage_ReMovingGhostHouseBlock(SLib.SpriteImage_PivotRotationControlled):  # 266, 696
    def __init__(self, parent):
        super().__init__(
            parent,
            3.75,
        )

    @staticmethod
    def loadImages():
        SLib.loadIfNotInImageCache('GhostHouseBlockT', 'ghost_house_block_t.png')
        SLib.loadIfNotInImageCache('GhostHouseBlockTL', 'ghost_house_block_tl.png')
        SLib.loadIfNotInImageCache('GhostHouseBlockTR', 'ghost_house_block_tr.png')
        SLib.loadIfNotInImageCache('GhostHouseBlockL', 'ghost_house_block_l.png')
        SLib.loadIfNotInImageCache('GhostHouseBlockM', 'ghost_house_block_m.png')
        SLib.loadIfNotInImageCache('GhostHouseBlockR', 'ghost_house_block_r.png')
        SLib.loadIfNotInImageCache('GhostHouseBlockB', 'ghost_house_block_b.png')
        SLib.loadIfNotInImageCache('GhostHouseBlockBL', 'ghost_house_block_bl.png')
        SLib.loadIfNotInImageCache('GhostHouseBlockBR', 'ghost_house_block_br.png')

    def dataChanged(self):

        self.affectImage = (self.parent.spritedata[3] & 1) != 1
        self.affectAUXImage = (self.parent.spritedata[3] & 1) != 1

        self.updateSize()

        pix = QtGui.QPixmap(self.width * 3.75, self.height * 3.75)
        pix.fill(Qt.transparent)

        painter = QtGui.QPainter(pix)

        # Draw middle
        painter.drawTiledPixmap(60, 60, (self.w - 2) * 60, (self.h - 2) * 60, ImageCache['GhostHouseBlockM'], 15, ImageCache['GhostHouseBlockM'].height() - (((self.h - 2) * 60) % ImageCache['GhostHouseBlockM'].height()))

        # Draw top row
        painter.drawPixmap(0, 0, ImageCache['GhostHouseBlockTL'])
        painter.drawTiledPixmap(60, 0, (self.w - 2) * 60, 60, ImageCache['GhostHouseBlockT'])
        painter.drawPixmap((self.w - 1) * 60, 0, ImageCache['GhostHouseBlockTR'])

        # Draw left and right side
        painter.drawTiledPixmap(0, 60, 60, (self.h - 2) * 60, ImageCache['GhostHouseBlockL'])
        painter.drawTiledPixmap((self.w - 1) * 60, 60, 60, (self.h - 2) * 60, ImageCache['GhostHouseBlockR'])

        # Draw bottom row
        painter.drawPixmap(0, (self.h - 1) * 60, ImageCache['GhostHouseBlockBL'])
        painter.drawTiledPixmap(60, (self.h - 1) * 60, (self.w - 2) * 60, 60, ImageCache['GhostHouseBlockB'])
        painter.drawPixmap((self.w - 1) * 60, (self.h - 1) * 60, ImageCache['GhostHouseBlockBR'])

        painter.end()
        del painter

        self.image = pix

        super().dataChanged()

    def updateSize(self):
        self.w = (self.parent.spritedata[8] & 0x1F) + 3
        self.h = (self.parent.spritedata[9] & 0x1F) + 3
        self.width = self.w << 4
        self.height = self.h << 4

class SpriteImage_GhostHouseRotatingRoom(SLib.SpriteImage_PivotRotationControlled):  # 731
    def __init__(self, parent):
        super().__init__(
            parent,
            3.75,
        )

        self.parent.setZValue(-40000)

    @staticmethod
    def loadImages():
        SLib.loadIfNotInImageCache('20x28', '20x28.png')
        SLib.loadIfNotInImageCache('23x32', '23x32.png')
        SLib.loadIfNotInImageCache('34x32', '34x32.png')

    def dataChanged(self):
        self.affectImage = (self.parent.spritedata[3] & 1) != 1
        self.affectAUXImage = (self.parent.spritedata[3] & 1) != 1

        style = self.parent.spritedata[5] & 0xF
         
        if style == 0:
            self.image = ImageCache['20x28']

            self.xOffset = 0
            self.yOffset = 0

        elif style == 1:
            self.image = ImageCache['23x32']

            self.xOffset = 0
            self.yOffset = 0
    
        else:
            self.image = ImageCache['34x32']

            self.xOffset = 0
            self.yOffset = 0
            

        super().dataChanged()

class SpriteImage_KoopaTroopa(SLib.SpriteImage_StaticMultiple):  # 19, 55
    def __init__(self, parent):
        super().__init__(
            parent,
            3.75,
        )

        self.xOffset = -4

    @staticmethod
    def loadImages():
        SLib.loadIfNotInImageCache('KoopaShellG', 'koopatroopa_shell_green.png')
        SLib.loadIfNotInImageCache('KoopaShellR', 'koopatroopa_shell_red.png')
        SLib.loadIfNotInImageCache('KoopatroopaG', 'koopatroopa_green.png')
        SLib.loadIfNotInImageCache('KoopatroopaR', 'koopatroopa_red.png')
        SLib.loadIfNotInImageCache('KoopatroopaGR', 'koopatroopa_green_r.png')
        SLib.loadIfNotInImageCache('KoopatroopaRR', 'koopatroopa_red_r.png')

    def dataChanged(self):
        direction = (self.parent.spritedata[4] & 0xF) == 2
        shellcolour = self.parent.spritedata[5] & 1
        inshell = (self.parent.spritedata[5] >> 4) & 1

        if inshell:
            self.offset = (-4, 0)
            self.image = ImageCache['KoopaShellR' if shellcolour else 'KoopaShellG']
        elif direction:
            self.offset = (0, -16)
            self.image = ImageCache['KoopatroopaRR' if shellcolour else 'KoopatroopaGR']
        else:
            self.offset = (-4, -16)
            self.image = ImageCache['KoopatroopaR' if shellcolour else 'KoopatroopaG']

        super().dataChanged()


class SpriteImage_VLimitL(SLib.SpriteImage_StaticMultiple):  # 27
    def __init__(self, parent):
        super().__init__(
            parent,
            3.75,
        )

    @staticmethod
    def loadImages():
        SLib.loadIfNotInImageCache('VLimitDl', 'vlimit_d_l.png')
        SLib.loadIfNotInImageCache('VLimitUL', 'vlimit_u_l.png')

    def dataChanged(self):

        direction = self.parent.spritedata[2]

        if direction == 0:
            self.dimensions = (0, 4, 0, 0)
            self.image = ImageCache['VLimitDl']
        elif direction == 16 or direction == 17 or direction == 18 or direction == 19 or direction == 20 or direction == 21 or direction == 22 or direction == 23 or direction == 24 or direction == 25 or direction == 26 or direction == 27 or direction == 28 or direction == 29 or direction == 30 or direction == 31:
            self.dimensions = (0, 0, 0, 0)
            self.image = ImageCache['VLimitUL']
        else:
            self.dimensions = (0, 4, 0, 0)
            self.image = ImageCache['VLimitDl']

        super().dataChanged()


class SpriteImage_VLimitR(SLib.SpriteImage_StaticMultiple):  # 28
    def __init__(self, parent):
        super().__init__(
            parent,
            3.75,
        )

    @staticmethod
    def loadImages():
        SLib.loadIfNotInImageCache('VLimitDR', 'vlimit_d_r.png')
        SLib.loadIfNotInImageCache('VLimitUR', 'vlimit_u_r.png')

    def dataChanged(self):

        direction = self.parent.spritedata[2]

        if direction == 0:
            self.dimensions = (0, 4, 0, 0)
            self.image = ImageCache['VLimitDR']
        elif direction == 16 or direction == 17 or direction == 18 or direction == 19 or direction == 20 or direction == 21 or direction == 22 or direction == 23 or direction == 24 or direction == 25 or direction == 26 or direction == 27 or direction == 28 or direction == 29 or direction == 30 or direction == 31:
            self.dimensions = (0, 0, 0, 0)
            self.image = ImageCache['VLimitUR']
        else:
            self.dimensions = (0, 4, 0, 0)
            self.image = ImageCache['VLimitDR']

        super().dataChanged()


class SpriteImage_LimitU(SLib.SpriteImage_StaticMultiple):  # 29
    def __init__(self, parent):
        super().__init__(
            parent,
            3.75,
        )

    @staticmethod
    def loadImages():
        SLib.loadIfNotInImageCache('LimitUR', 'limit_u_r.png')
        SLib.loadIfNotInImageCache('LimitUL', 'limit_u_l.png')

    def dataChanged(self):

        direction = self.parent.spritedata[2]

        if direction == 0:
            self.dimensions = (4, 0, 0, 0)
            self.image = ImageCache['LimitUR']
        elif direction == 16 or direction == 17 or direction == 18 or direction == 19 or direction == 20 or direction == 21 or direction == 22 or direction == 23 or direction == 24 or direction == 25 or direction == 26 or direction == 27 or direction == 28 or direction == 29 or direction == 30 or direction == 31:
            self.dimensions = (0, 0, 0, 0)
            self.image = ImageCache['LimitUL']
        else:
            self.dimensions = (4, 0, 0, 0)
            self.image = ImageCache['LimitUR']

        super().dataChanged()


class SpriteImage_LimitD(SLib.SpriteImage_StaticMultiple):  # 30
    def __init__(self, parent):
        super().__init__(
            parent,
            3.75,
        )

    @staticmethod
    def loadImages():
        SLib.loadIfNotInImageCache('LimitDR', 'limit_d_r.png')
        SLib.loadIfNotInImageCache('LimitDL', 'limit_d_l.png')

    def dataChanged(self):

        direction = self.parent.spritedata[2]

        if direction == 0:
            self.dimensions = (4, 0, 0, 0)
            self.image = ImageCache['LimitDR']
        elif direction == 16 or direction == 17 or direction == 18 or direction == 19 or direction == 20 or direction == 21 or direction == 22 or direction == 23 or direction == 24 or direction == 25 or direction == 26 or direction == 27 or direction == 28 or direction == 29 or direction == 30 or direction == 31:
            self.dimensions = (0, 0, 0, 0)
            self.image = ImageCache['LimitDL']
        else:
            self.dimensions = (4, 0, 0, 0)
            self.image = ImageCache['LimitDR']

        super().dataChanged()


class SpriteImage_MovementStarCoin(SLib.SpriteImage_MovementControlled):  # 48
    def __init__(self, parent):
        super().__init__(
            parent,
            3.75,
        )

        self.previousType = 0
        self.yOffset = 8

    @staticmethod
    def loadImages():
        SLib.loadIfNotInImageCache('StarCoin', 'star_coin.png')

    def getMovementType(self):
        return self.parent.spritedata[9] >> 4 & 3

    def allowedMovementControllers(self):
        if self.getMovementType() == 0:
            return 68, 116, 69, 118

        return tuple()

    def dataChanged(self):
        type = self.getMovementType()
        if type != self.previousType:
            self.previousType = type
            self.unhookController()

        if type == 0:
            self.offset = (-16, -10)

        else:
            self.offset = (0, 6)

        self.image = ImageCache['StarCoin']

        super().dataChanged()


class SpriteImage_Path(SLib.SpriteImage_StaticMultiple):  # 100
    def __init__(self, parent):
        super().__init__(
            parent,
            3.75,
            ImageCache['Path'],
            (0, 0),
        )

    @staticmethod
    def loadImages():
        SLib.loadIfNotInImageCache('Path', 'path.png')


class SpriteImage_ControllerSwaying_Path(SLib.SpriteImage_MovementController):  # 116
    def __init__(self, parent):
        super().__init__(
            parent,
            3.75,
            ImageCache['ControllerSwaying_Path'],
        )

        self.aux.append(SLib.AuxiliaryRotationAreaOutline(parent, 60))
        self.aux.append(SLib.AuxiliaryRotationAreaOutline(parent, 120))

        self.rotation = 0
        self.startOffset = 0
        self.arc = 0
        self.eventActivated = False

    @staticmethod
    def loadImages():
        SLib.loadIfNotInImageCache('ControllerSwaying_Path', 'controller_swaying_path.png')

    def dataChanged(self):
        self.startOffset = (self.parent.spritedata[2] & 0xF) * 22.5 + 90
        self.eventActivated = (self.parent.spritedata[4] & 0x40) != 0
        reversedDir = ((self.parent.spritedata[4] >> 4) & 1) != 0
        self.arcMiddleRotation = (self.parent.spritedata[4] & 0xF) * 22.5
        self.delay = self.parent.spritedata[6] & 0xF0
        self.arc = (self.parent.spritedata[7] >> 4) * 22.5
        self.rotationSpeed = ((self.parent.spritedata[7] & 0xF) / 0x800) * 360

        if reversedDir:
            self.startOffset += 180
        
        self.rotation = math.cos(math.radians(self.startOffset))
            
        self.aux[0].SetAngle(90 + self.arcMiddleRotation - self.arc * 0.5, self.arc)
        self.aux[1].SetAngle(90 + self.arcMiddleRotation - self.rotation * self.arc * 0.5, 0)

        super().dataChanged()

    def active(self):
        return not self.eventActivated

    def getStartRotation(self):
        if not self.eventActivated:
            self.rotation = math.cos(math.radians(self.startOffset - SLib.RotationFrame * self.rotationSpeed * (60 / SLib.RotationFPS)))

        return -self.arcMiddleRotation + self.rotation * self.arc * 0.5


class SpriteImage_ControllerSpinning_Path(SLib.SpriteImage_MovementController):  # 118
    Speeds = [0x400000, 0x800000, 0xc00000, 0x1000000, 0x200000, 0x2000000, 0x4000000, 0x100000]

    def __init__(self, parent):
        super().__init__(
            parent,
            3.75,
            ImageCache['ControllerSpinning_Path'],
        )
        self.aux.append(SLib.AuxiliaryRotationAreaOutline(parent, 60))
        self.aux.append(SLib.AuxiliaryRotationAreaOutline(parent, 120))

    @staticmethod
    def loadImages():
        SLib.loadIfNotInImageCache('ControllerSpinning_Path', 'controller_spinning_path.png')

    def dataChanged(self):
        self.rotation = (self.parent.spritedata[2] >> 4) * 22.5
        arc = (self.parent.spritedata[7] >> 4) * 22.5
        self.spinMode = self.parent.spritedata[3] & 3
        reversedDir = self.parent.spritedata[7] & 0xF > 7
        speedValue = self.parent.spritedata[7] & 0xF

        if speedValue > 7:
            speedValue -= 8

        self.rotationSpeed = (SpriteImage_ControllerSpinning_Path.Speeds[speedValue] / 0x100000000) * 360

        if reversedDir:
            self.rotation = -self.rotation
            self.rotationSpeed = -self.rotationSpeed

        if self.spinMode == 1:
            arc = 360

        self.aux[0].SetAngle(90 + self.rotation - (arc if reversedDir else 0), arc)
        self.aux[1].SetAngle(90 + self.rotation, 0)
        self.parent.updateScene()
        super().dataChanged()

    def active(self):
        return self.spinMode == 1

    def getStartRotation(self):
        if self.spinMode == 1:
            return -self.rotation - SLib.RotationFrame * self.rotationSpeed * (60 / SLib.RotationFPS)
        else:
            return -self.rotation
        

class SpriteImage_FallingIcicle(SLib.SpriteImage_StaticMultiple):  # 183
    def __init__(self, parent):
        super().__init__(
            parent,
            3.75,
        )

        self.yOffset = -4

    @staticmethod
    def loadImages():
        SLib.loadIfNotInImageCache('FallingIcicle1', 'falling_icicle_1.png')
        SLib.loadIfNotInImageCache('FallingIcicle2', 'falling_icicle_2.png')

    def dataChanged(self):
        size = self.parent.spritedata[5]

        if size == 1:
            self.image = ImageCache['FallingIcicle2']
        else:
            self.image = ImageCache['FallingIcicle1']

        super().dataChanged()


class SpriteImage_BossController(SLib.SpriteImage_StaticMultiple):  # 216, 245, 412, 432, 435, 466, 497
    def __init__(self, parent):
        super().__init__(
            parent,
            3.75,
            ImageCache['BossController'],
            (0, 0),
        )

    @staticmethod
    def loadImages():
        SLib.loadIfNotInImageCache('BossController', 'boss_controller.png')


class SpriteImage_Bush(SLib.SpriteImage_StaticMultiple):  # 288
    colors = (
        ('Green', 'green'),
        ('Yellow', 'yellow'),
    )

    offsets = (
        (-28, -32),
        (-36, -44),
        (-32, -60),
        (-40, -76),
    )

    def __init__(self, parent):
        super().__init__(
            parent,
            3.75,
        )

        self.parent.setZValue(-60000)

    @staticmethod
    def loadImages():
        for C, c in SpriteImage_Bush.colors:
            for i in range(4):
                SLib.loadIfNotInImageCache('Bush%s%d' % (C, i), 'bush_%d_%s.png' % (i, c))

    def dataChanged(self):
        type = self.parent.spritedata[5] & 3
        isYellow = self.parent.spritedata[5] >> 4 & 1

        self.image = ImageCache['Bush%s%d' % (SpriteImage_Bush.colors[isYellow][0], type)]
        self.offset = SpriteImage_Bush.offsets[type]

        super().dataChanged()


class SpriteImage_GiantWiggler(SLib.SpriteImage_StaticMultiple):  # 301
    def __init__(self, parent):
        super().__init__(
            parent,
            3.75,
        )

    @staticmethod
    def loadImages():
        SLib.loadIfNotInImageCache('GiantWiggler', 'giant_wiggler.png')
        SLib.loadIfNotInImageCache('GiantWigglerR', 'giant_wiggler_r.png')

    def dataChanged(self):
        direction = (self.parent.spritedata[5] >> 4)

        if direction == 1:
            self.offset = (-136, -72)
            self.image = ImageCache['GiantWigglerR']
        else:
            self.offset = (-32, -72)
            self.image = ImageCache['GiantWiggler']

        super().dataChanged()


class SpriteImage_DashCoin(SLib.SpriteImage_Static):  # 325
    def __init__(self, parent):
        super().__init__(
            parent,
            3.75,
            ImageCache['DashCoin'],
            (0, 0),
        )

    @staticmethod
    def loadImages():
        SLib.loadIfNotInImageCache('DashCoin', 'outline.png')


class SpriteImage_LavaBlock(SLib.SpriteImage_StaticMultiple):  # 359
    def __init__(self, parent):
        super().__init__(
            parent,
            3.75,
        )

        self.parent.setZValue(-40000)

    @staticmethod
    def loadImages():
        SLib.loadIfNotInImageCache('type_0', 'lavablock_0.png')
        SLib.loadIfNotInImageCache('type_1', 'lavablock_1.png')
        SLib.loadIfNotInImageCache('type_2', 'lavablock_2.png')
        SLib.loadIfNotInImageCache('type_3', 'lavablock_3.png')
        SLib.loadIfNotInImageCache('type_4', 'lavablock_4.png')
        SLib.loadIfNotInImageCache('type_5', 'lavablock_5.png')
        SLib.loadIfNotInImageCache('type_6', 'lavablock_6.png')
        SLib.loadIfNotInImageCache('type_7', 'lavablock_7.png')
        SLib.loadIfNotInImageCache('type_8', 'lavablock_8.png')
        SLib.loadIfNotInImageCache('type_9', 'lavablock_9.png')
        SLib.loadIfNotInImageCache('type_10', 'lavablock_10.png')
        SLib.loadIfNotInImageCache('type_11', 'crash.png')

    def dataChanged(self):
        type = self.parent.spritedata[4]

        if type == 1:
            self.image = ImageCache['type_1']
        elif type == 2:
            self.image = ImageCache['type_2']
        elif type == 3:
            self.image = ImageCache['type_3']
        elif type == 4:
            self.image = ImageCache['type_4']
        elif type == 5:
            self.image = ImageCache['type_5']
        elif type == 6:
            self.image = ImageCache['type_6']
        elif type == 7:
            self.image = ImageCache['type_7']
        elif type == 8:
            self.image = ImageCache['type_8']
        elif type == 9:
            self.image = ImageCache['type_9']
        elif type == 10:
            self.image = ImageCache['type_10']
        elif type == 11:
            self.image = ImageCache['type_11']
        elif type == 12:
            self.image = ImageCache['type_11']
        else:   
            self.image = ImageCache['type_0']

        super().dataChanged()


class SpriteImage_Debris(SLib.SpriteImage_StaticMultiple):  # 440
    def __init__(self, parent):
        super().__init__(
            parent,
            3.75
        )

        self.aux.append(SLib.AuxiliaryImage(parent, 1, 1))

    @staticmethod
    def loadImages():
        SLib.loadIfNotInImageCache('Debris_Small', 'debris_small.png')
        SLib.loadIfNotInImageCache('Debris_Big', 'debris_big.png')
        SLib.loadIfNotInImageCache('Debris_Both', 'debris_both.png')

    def dataChanged(self):
        type = (self.parent.spritedata[5] & 0xF)

        if type == 1:
            self.dimensions = (-32, -24, 64, 64)
            self.aux[0].setImage(ImageCache['Debris_Big'], -360, -420)
        elif type == 2:
            self.dimensions = (-32, -24, 64, 64)
            self.aux[0].setImage(ImageCache['Debris_Both'], -360, -420)
        else:
            self.dimensions = (-16, -8, 32, 32)
            self.aux[0].setImage(ImageCache['Debris_Small'], -180, -210)

        super().dataChanged()


class SpriteImage_KamekBlock(SLib.SpriteImage_StaticMultiple):  # 450
    def __init__(self, parent):
        super().__init__(
            parent,
            3.75,
            ImageCache['KamekBlock'],
            (0, -32),
        )

    @staticmethod
    def loadImages():
        SLib.loadIfNotInImageCache('KamekBlock', 'kamek_block.png')


class SpriteImage_GiantKoopaTroopa(SLib.SpriteImage_StaticMultiple):  # 476
    def __init__(self, parent):
        super().__init__(
            parent,
            3.75,
        )

    @staticmethod
    def loadImages():
        SLib.loadIfNotInImageCache('GiantKoopaShellG', 'giant_koopatroopa_shell_green.png')
        SLib.loadIfNotInImageCache('GiantKoopaShellR', 'giant_koopatroopa_shell_red.png')
        SLib.loadIfNotInImageCache('GiantKoopatroopaG', 'giant_koopatroopa_green.png')
        SLib.loadIfNotInImageCache('GiantKoopatroopaR', 'giant_koopatroopa_red.png')
        SLib.loadIfNotInImageCache('GiantKoopatroopaGR', 'giant_koopatroopa_green_r.png')
        SLib.loadIfNotInImageCache('GiantKoopatroopaRR', 'giant_koopatroopa_red_r.png')

    def dataChanged(self):
        direction = (self.parent.spritedata[4] & 0xF) == 2
        shellcolour = self.parent.spritedata[5] & 1
        inshell = (self.parent.spritedata[5] >> 4) & 1

        if inshell:
            self.offset = (-12, -16)
            self.image = ImageCache['GiantKoopaShellR' if shellcolour else 'GiantKoopaShellG']
        elif direction:
            self.offset = (-6, -40)
            self.image = ImageCache['GiantKoopatroopaRR' if shellcolour else 'GiantKoopatroopaGR']
        else:
            self.offset = (-24, -40)
            self.image = ImageCache['GiantKoopatroopaR' if shellcolour else 'GiantKoopatroopaG']

        super().dataChanged()


class SpriteImage_FloatingBarrel(SLib.SpriteImage_StaticMultiple):  # 522
    def __init__(self, parent):
        super().__init__(
            parent,
            3.75
        )

    @staticmethod
    def loadImages():
        SLib.loadIfNotInImageCache('Floating_Barrel', 'floating_barrel.png')
        SLib.loadIfNotInImageCache('Floating_Barrel_Large', 'floating_barrel_large.png')

    def dataChanged(self):

        if self.parent.spritedata[5] & 1:
            self.offset = (-40, -24)
            self.image = ImageCache['Floating_Barrel_Large']
        else:
            self.offset = (-16, -12)
            self.image = ImageCache['Floating_Barrel']

        super().dataChanged()


class SpriteImage_GoalRing(SLib.SpriteImage_StaticMultiple):  # 599
    def __init__(self, parent):
        super().__init__(
            parent,
            3.75,
            ImageCache['GoalRing'],
            (-16, -48),
        )

    @staticmethod
    def loadImages():
        SLib.loadIfNotInImageCache('GoalRing', 'goal_ring.png')

class SpriteImage_CoinSnake(SLib.SpriteImage_StaticMultiple):  # 522
    def __init__(self, parent):
        super().__init__(
            parent,
            3.75,
            ImageCache['qbl0'],
        )

    @staticmethod
    def loadImages():
        SLib.loadIfNotInImageCache('coin', 'coin.png')
        SLib.loadIfNotInImageCache('starcoin', 'star_coin.png')
        SLib.loadIfNotInImageCache('qbl16', 'qbl16.png')
        for j in range(16):
            SLib.loadIfNotInImageCache('qbl{0}'.format(j),
                                        'qbl{0}.png'.format(j))

    def dataChanged(self):
        qblAcn = self.parent.spritedata[6] >> 4
        stcType = self.parent.spritedata[3] & 0xF
        qblType = self.parent.spritedata[9] >> 4
        qblCts = self.parent.spritedata[9] & 0xF

        self.w = ((self.parent.spritedata[8] & 0x0F) * 3) + 5
        self.width = (self.w << 4)


        pix = QtGui.QPixmap((((stcType==1)* 90)+((stcType==2)* 90)+((stcType==3)* 30)) + (self.width * 7.5 - 60), (((stcType!=0)+1)*60))
        pix.fill(Qt.transparent)

        painter = QtGui.QPainter(pix)

        self.updateSize()

        if stcType != 0:
                if stcType == 1:
                    for i in range(self.w):
                        self.updateSize()
                        self.offset = (-16, -16)
                        if i == 0:
                            painter.drawTiledPixmap(i * 120, 0, 120, 120, ImageCache['starcoin'])
                    else:
                        if qblType <= 1:
                            for i in range(self.w):
                                self.updateSize()
                                painter.drawTiledPixmap((i + 1.75) * 120, 30, 60, 60, ImageCache['coin'])
                        elif qblType == 2:
                            for j in range(self.w):
                                self.updateSize()
                                if j == 0:
                                    self.image = ImageCache['coin']
                                elif j == (self.w) - 1:
                                    painter.drawTiledPixmap((j+.75) * 120, (stcType!=0)*30, 60, 60, ImageCache['qbl{0}'.format(qblCts)])
                                else:
                                    painter.drawTiledPixmap((j+.75) * 120, (stcType!=0)*30, 60, 60, ImageCache['coin'])
                        elif qblType == 3:
                            for j in range(self.w):
                                self.updateSize()
                                if j == 0:
                                    self.image = ImageCache['coin']
                                elif j % 3 == 0:
                                    painter.drawTiledPixmap((j+.75) * 120, (stcType!=0)*30, 60, 60, ImageCache['qbl1'])
                                else:
                                    painter.drawTiledPixmap((j+.75) * 120, (stcType!=0)*30, 60, 60, ImageCache['coin'])
                        elif qblType == 4:
                            for j in range(self.w):
                                self.updateSize()
                                if j == 0:
                                    self.image = ImageCache['coin']
                                elif j % 4 == 0:
                                    painter.drawTiledPixmap((j+.75) * 120, (stcType!=0)*30, 60, 60, ImageCache['qbl1'])
                                else:
                                    painter.drawTiledPixmap((j+.75) * 120, (stcType!=0)*30, 60, 60, ImageCache['coin'])
                        else:
                            for j in range(self.w):
                                self.updateSize()
                                if j == 0:
                                    self.image = ImageCache['coin']
                                elif j % 5 == 0:
                                    painter.drawTiledPixmap((j+.75) * 120, (stcType!=0)*30, 60, 60, ImageCache['qbl1'])
                                else:
                                    painter.drawTiledPixmap((j+.75) * 120, (stcType!=0)*30, 60, 60, ImageCache['coin'])
                elif stcType == 2:
                    for i in range(self.w):
                        self.updateSize()
                        self.offset = (-8, -16)
                        if i == self.w - 1:
                            painter.drawTiledPixmap((i + .25) * 120, 0, 120, 120, ImageCache['starcoin'])
                    else:
                        if qblType == 0:
                            for i in range(self.w):
                                self.updateSize()
                                if i == (self.w) - 1:
                                    self.image = ImageCache['coin']
                                else:
                                    painter.drawTiledPixmap(i * 120, 30, 60, 60, ImageCache['coin'])
                        elif qblType == 1:
                            for j in range(self.w):
                                self.updateSize()
                                if j == (self.w) - 1:
                                    self.image = ImageCache['coin']
                                elif j == 0:
                                    painter.drawTiledPixmap(j * 120, (stcType!=0)*30, 60, 60, ImageCache['qbl{0}'.format(qblCts)])
                                else:
                                    painter.drawTiledPixmap(j * 120, (stcType!=0)*30, 60, 60, ImageCache['coin'])
                        elif qblType == 2:
                            for i in range(self.w):
                                self.updateSize()
                                if i == (self.w) - 1:
                                    self.image = ImageCache['coin']
                                else:
                                    painter.drawTiledPixmap(i * 120, 30, 60, 60, ImageCache['coin'])
                        elif qblType == 3:
                            for j in range(self.w):
                                self.updateSize()
                                if j == (self.w) - 1:
                                    self.image = ImageCache['coin']
                                elif j % 3 == 0:
                                    if j == 0:
                                        painter.drawTiledPixmap(j * 120, (stcType!=0)*30, 60, 60, ImageCache['qbl{0}'.format(qblCts)])
                                    else:
                                        painter.drawTiledPixmap(j * 120, (stcType!=0)*30, 60, 60, ImageCache['qbl1'])
                                else:
                                    painter.drawTiledPixmap(j * 120, (stcType!=0)*30, 60, 60, ImageCache['coin'])
                        elif qblType == 4:
                            for j in range(self.w):
                                self.updateSize()
                                if j == (self.w) - 1:
                                    self.image = ImageCache['coin']
                                elif j % 4 == 0:
                                    if j == 0:
                                        painter.drawTiledPixmap(j * 120, (stcType!=0)*30, 60, 60, ImageCache['qbl{0}'.format(qblCts)])
                                    else:
                                        painter.drawTiledPixmap(j * 120, (stcType!=0)*30, 60, 60, ImageCache['qbl1'])
                                else:
                                    painter.drawTiledPixmap(j * 120, (stcType!=0)*30, 60, 60, ImageCache['coin'])
                        else:
                            for j in range(self.w):
                                self.updateSize()
                                if j == (self.w) - 1:
                                    self.image = ImageCache['coin']
                                elif j % 5 == 0:
                                    if j == 0:
                                        painter.drawTiledPixmap(j * 120, (stcType!=0)*30, 60, 60, ImageCache['qbl{0}'.format(qblCts)])
                                    else:
                                        painter.drawTiledPixmap(j * 120, (stcType!=0)*30, 60, 60, ImageCache['qbl1'])
                                else:
                                    painter.drawTiledPixmap(j * 120, (stcType!=0)*30, 60, 60, ImageCache['coin'])
                else:
                    for i in range(self.w):
                        self.updateSize()
                        self.offset = (-8, -16)
                        if i == self.w - 1:
                            painter.drawTiledPixmap((i - 0.25) * 120, 0, 120, 120, ImageCache['starcoin'])
                    else:
                        if qblType == 0:
                            for i in range(self.w):
                                self.updateSize()
                                if i == (self.w) - 1:
                                    self.image = ImageCache['coin']
                                else:
                                    painter.drawTiledPixmap(i * 120, 30, 60, 60, ImageCache['coin'])
                        elif qblType == 1:
                            for j in range(self.w):
                                self.updateSize()
                                if j == (self.w) - 1:
                                    self.image = ImageCache['coin']
                                elif j == 0:
                                    painter.drawTiledPixmap(j * 120, (stcType!=0)*30, 60, 60, ImageCache['qbl{0}'.format(qblCts)])
                                else:
                                    painter.drawTiledPixmap(j * 120, (stcType!=0)*30, 60, 60, ImageCache['coin'])
                        elif qblType == 2:
                            for i in range(self.w):
                                self.updateSize()
                                if i == (self.w) - 1:
                                    self.image = ImageCache['coin']
                                else:
                                    painter.drawTiledPixmap(i * 120, 30, 60, 60, ImageCache['coin'])
                        elif qblType == 3:
                            for j in range(self.w):
                                self.updateSize()
                                if j == (self.w) - 1:
                                    self.image = ImageCache['coin']
                                elif j % 3 == 0:
                                    if j == 0:
                                        painter.drawTiledPixmap(j * 120, (stcType!=0)*30, 60, 60, ImageCache['qbl{0}'.format(qblCts)])
                                    else:
                                        painter.drawTiledPixmap(j * 120, (stcType!=0)*30, 60, 60, ImageCache['qbl1'])
                                else:
                                    painter.drawTiledPixmap(j * 120, (stcType!=0)*30, 60, 60, ImageCache['coin'])
                        elif qblType == 4:
                            for j in range(self.w):
                                self.updateSize()
                                if j == (self.w) - 1:
                                    self.image = ImageCache['coin']
                                elif j % 4 == 0:
                                    if j == 0:
                                        painter.drawTiledPixmap(j * 120, (stcType!=0)*30, 60, 60, ImageCache['qbl{0}'.format(qblCts)])
                                    else:
                                        painter.drawTiledPixmap(j * 120, (stcType!=0)*30, 60, 60, ImageCache['qbl1'])
                                else:
                                    painter.drawTiledPixmap(j * 120, (stcType!=0)*30, 60, 60, ImageCache['coin'])
                        else:
                            for j in range(self.w):
                                self.updateSize()
                                if j == (self.w) - 1:
                                    self.image = ImageCache['coin']
                                elif j % 5 == 0:
                                    if j == 0:
                                        painter.drawTiledPixmap(j * 120, (stcType!=0)*30, 60, 60, ImageCache['qbl{0}'.format(qblCts)])
                                    else:
                                        painter.drawTiledPixmap(j * 120, (stcType!=0)*30, 60, 60, ImageCache['qbl1'])
                                else:
                                    painter.drawTiledPixmap(j * 120, (stcType!=0)*30, 60, 60, ImageCache['coin'])  
        else:
            if qblType != 0:
                self.offset = (-8, -8)
                if qblType == 1:
                        for i in range(self.w):
                            self.updateSize()
                            if i == 0:
                                painter.drawTiledPixmap(i * 120, (stcType!=0)*30, 60, 60, ImageCache['qbl{0}'.format(qblCts)])
                            else:
                                painter.drawTiledPixmap(i * 120, (stcType!=0)*30, 60, 60, ImageCache['coin'])
                elif qblType == 2:
                        for i in range(self.w):
                            self.updateSize()
                            if i == (self.w) - 1:
                                painter.drawTiledPixmap(i * 120, (stcType!=0)*30, 60, 60, ImageCache['qbl{0}'.format(qblCts)])
                            else:
                                painter.drawTiledPixmap(i * 120, (stcType!=0)*30, 60, 60, ImageCache['coin'])
                elif qblType == 3:
                        for i in range(self.w):
                            self.updateSize()
                            if i == 0:
                                painter.drawTiledPixmap(i * 120, (stcType!=0)*30, 60, 60, ImageCache['qbl{0}'.format(qblCts)])
                            else:
                                if i % 3 == 0:
                                    painter.drawTiledPixmap(i * 120, (stcType!=0)*30, 60, 60, ImageCache['qbl1'])
                                else:
                                    painter.drawTiledPixmap(i * 120, (stcType!=0)*30, 60, 60, ImageCache['coin'])
                elif qblType == 4:
                        for i in range(self.w):
                            self.updateSize()
                            if i == 0:
                                painter.drawTiledPixmap(i * 120, (stcType!=0)*30, 60, 60, ImageCache['qbl{0}'.format(qblCts)])
                            else:
                                if i % 4 == 0:
                                    painter.drawTiledPixmap(i * 120, (stcType!=0)*30, 60, 60, ImageCache['qbl1'])
                                else:
                                    painter.drawTiledPixmap(i * 120, (stcType!=0)*30, 60, 60, ImageCache['coin'])
                else:    
                        for i in range(self.w):
                            self.updateSize()
                            if i == 0:
                                painter.drawTiledPixmap(i * 120, (stcType!=0)*30, 60, 60, ImageCache['qbl{0}'.format(qblCts)])
                            else:
                                if i % 5 == 0:
                                    painter.drawTiledPixmap(i * 120, (stcType!=0)*30, 60, 60, ImageCache['qbl1'])
                                else:
                                    painter.drawTiledPixmap(i * 120, (stcType!=0)*30, 60, 60, ImageCache['coin'])    
            else:  
                self.offset = (-8, -8)
                for i in range(self.w):
                    self.updateSize()

                    painter.drawTiledPixmap(i * 120, 0, 60, 60, ImageCache['coin'])

        painter.end()
        del painter

        self.image = pix
        super().dataChanged()

    def updateSize(self):
        self.w = ((self.parent.spritedata[8] & 0x0F) * 3) + 5
        self.width = (self.w << 4)

class SpriteImage_GrayCrystal(SLib.SpriteImage_PivotRotationControlled):  # 391
    def __init__(self, parent):
        super().__init__(
            parent,
            3.75,
        )

    @staticmethod
    def loadImages():
        SLib.loadIfNotInImageCache('GrayCrystalH0', 'crystal_gray_h_0.png')
        SLib.loadIfNotInImageCache('GrayCrystalH1', 'crystal_gray_h_1.png')
        SLib.loadIfNotInImageCache('GrayCrystalH2', 'crystal_gray_h_2.png')
        SLib.loadIfNotInImageCache('GrayCrystalH3', 'crystal_gray_h_3.png')
        SLib.loadIfNotInImageCache('GrayCrystalH4', 'crystal_gray_h_4.png')
        SLib.loadIfNotInImageCache('GrayCrystalV0', 'crystal_gray_v_0.png')
        SLib.loadIfNotInImageCache('GrayCrystalV1', 'crystal_gray_v_1.png')
        SLib.loadIfNotInImageCache('GrayCrystalV2', 'crystal_gray_v_2.png')
        SLib.loadIfNotInImageCache('GrayCrystalV3', 'crystal_gray_v_3.png')
        SLib.loadIfNotInImageCache('GrayCrystalV4', 'crystal_gray_v_4.png')

    def dataChanged(self):
        crystalType = self.parent.spritedata[4] & 0xf
        crystalRot = 'V' if ((self.parent.spritedata[5] >> 4) & 1) != 0 else 'H'
        if crystalType >= 5:
            self.image = ImageCache['GrayCrystal%s0' % crystalRot]
        else:
            self.image = ImageCache['GrayCrystal%s%d' % (crystalRot, crystalType)]

            if crystalRot == 'H':
                self.xOffset = -4
                self.yOffset = -4
            elif crystalType == 0:
                self.xOffset = 4
                self.yOffset = -12
            elif crystalType == 4:
                self.xOffset = 60
                self.yOffset = -68
            elif crystalType == 2:
                self.xOffset = 44
                self.yOffset = -52
            else:
                self.xOffset = 28
                self.yOffset = -36
        
        super().dataChanged()

class SpriteImage_PivotaBlock(SLib.SpriteImage_PivotRotationControlled):  # 522
    def __init__(self, parent):
        super().__init__(
            parent,
            3.75,
            ImageCache['qbl0'],
        )

    @staticmethod
    def loadImages():
        SLib.loadIfNotInImageCache('qbl16', 'qbl16.png')
        for j in range(16):
            SLib.loadIfNotInImageCache('qbl{0}'.format(j),
                                        'qbl{0}.png'.format(j))

    def dataChanged(self):
        self.affectImage = (self.parent.spritedata[2] & 0x2) != 2
        self.affectAUXImage = (self.parent.spritedata[2] & 0x2) != 2
        qblUD = self.parent.spritedata[2] & 0x1
        qblGR = self.parent.spritedata[2] & 0x2
        qblTL = self.parent.spritedata[2] & 0x4
        qblCts = self.parent.spritedata[9] & 0xF
        qblAcn = self.parent.spritedata[6] >> 4 & 0x1

        pix = QtGui.QPixmap(60, 60 + (30*qblGR))
        pix.fill(Qt.transparent)

        painter = QtGui.QPainter(pix)
        self.xOffset = 0
        if qblGR == 2:
            self.yOffset = 0
        else:
            if qblUD == 1:
                self.yOffset = 16
            else:
                self.yOffset = 0
        if qblAcn == 1:
            if qblCts != 0:
                painter.drawTiledPixmap(0, 0, 60, 60, ImageCache['qbl0'])
            else:
                painter.drawTiledPixmap(0, 0, 60, 60, ImageCache['qbl16'])
        else:
            painter.drawTiledPixmap(0, 0, 60, 60, ImageCache['qbl{0}'.format(qblCts)])

        painter.end()
        del painter

        self.image = pix
        super().dataChanged()

class SpriteImage_PivotaBrick(SLib.SpriteImage_PivotRotationControlled):  # 522
    def __init__(self, parent):
        super().__init__(
            parent,
            3.75,
            ImageCache['brk0'],
        )

    @staticmethod
    def loadImages():
        SLib.loadIfNotInImageCache('brk16', 'brk16.png')
        for j in range(16):
            SLib.loadIfNotInImageCache('brk{0}'.format(j),
                                        'brk{0}.png'.format(j))

    def dataChanged(self):
        self.affectImage = (self.parent.spritedata[2] & 0x2) != 2
        self.affectAUXImage = (self.parent.spritedata[2] & 0x2) != 2
        brkUD = self.parent.spritedata[2] & 0x1
        brkGR = self.parent.spritedata[2] & 0x2
        brkTL = self.parent.spritedata[2] & 0x4
        brkCts = self.parent.spritedata[9] & 0xF
        brkAcn = self.parent.spritedata[6] >> 4 & 0x1

        pix = QtGui.QPixmap(60, 60 + (30*brkGR))
        pix.fill(Qt.transparent)

        painter = QtGui.QPainter(pix)
        self.xOffset = 0
        if brkGR == 2:
            self.yOffset = 0
        else:
            if brkUD == 1:
                self.yOffset = 16
            else:
                self.yOffset = 0
        if brkAcn == 1:
            if brkCts != 0:
                painter.drawTiledPixmap(0, 0, 60, 60, ImageCache['brk0'])
            else:
                painter.drawTiledPixmap(0, 0, 60, 60, ImageCache['brk16'])
        else:
            painter.drawTiledPixmap(0, 0, 60, 60, ImageCache['brk{0}'.format(brkCts)])

        painter.end()
        del painter

        self.image = pix
        super().dataChanged()

class SpriteImage_Poltergeist(SLib.SpriteImage_Static):  # 305
    def __init__(self, parent):
        super().__init__(
            parent,
            3.75,
            ImageCache['Poltergeist'],
        )

    @staticmethod
    def loadImages():
        SLib.loadIfNotInImageCache('Poltergeist', 'poltergeist.png')
        SLib.loadIfNotInImageCache('Candlestick', 'candlestick.png')

    def dataChanged(self):

        if self.parent.spritedata[5] & 1:
            self.offset = (8, -16)
            self.image = ImageCache['Candlestick']
        else:
            self.offset = (0, 0)
            self.image = ImageCache['Poltergeist']

        super().dataChanged()

class SpriteImage_Candlestick(SLib.SpriteImage_Static):  # 305
    def __init__(self, parent):
        super().__init__(
            parent,
            3.75,
            ImageCache['Candlestick'],
            (8, -16),
        )

    @staticmethod
    def loadImages():
        SLib.loadIfNotInImageCache('Candlestick', 'candlestick.png')

ImageClasses = {
    724: SpriteImage_ActorSpawner,
    748: SpriteImage_MassiveSpikedStake,
    725: SpriteImage_Parabones,
    733: SpriteImage_Cataquack,
    738: SpriteImage_RainbowLight,
    726: SpriteImage_CustomDoor,
    727: SpriteImage_FakeActor,
    730: SpriteImage_BeepBlock,
    734: SpriteImage_TimeClock,
    749: SpriteImage_Scuttlebug,
    758: SpriteImage_Biddybud,
    760: SpriteImage_BasaltBones,
    770: SpriteImage_Peepa,
    729: SpriteImage_StarCoinShard,
    743: SpriteImage_Kamiya,
    731: SpriteImage_Chestnut,
    761: SpriteImage_Flaptor,
    753: SpriteImage_ColdFuzzy,
    766: SpriteImage_TripleBlock,
    360: SpriteImage_ActrSpawner,
    358: SpriteImage_FakActor,
    345: SpriteImage_TiltGirder,
    202: SpriteImage_PropellerBlock,
    529: SpriteImage_Crowber,
    199: SpriteImage_GlwBlock,
    319: SpriteImage_Metealbox,
    267: SpriteImage_KoopaCave,
    377: SpriteImage_LightGem,
    312: SpriteImage_CubeM,
    538: SpriteImage_RotoDisc,
    189: SpriteImage_LakituBlock,
    256: SpriteImage_MushroomCube,
    177: SpriteImage_SmallCannon,
    178: SpriteImage_BigCannon,
    274: SpriteImage_ColoredBlock,
    263: SpriteImage_PipeBubbles,
    405: SpriteImage_Kumiawase,
    434: SpriteImage_PivotalIronBlock,
    512: SpriteImage_GhostShipBlock,
    266: SpriteImage_ReMovingGhostHouseBlock,
    439: SpriteImage_GhostHouseRotatingRoom,
    436: SpriteImage_CubeM,
    19: SpriteImage_KoopaTroopa,
    27: SpriteImage_VLimitL,
    28: SpriteImage_VLimitR,
    29: SpriteImage_LimitU,
    30: SpriteImage_LimitD,
    55: SpriteImage_KoopaTroopa,
    48: SpriteImage_MovementStarCoin,
    100: SpriteImage_Path,
    116: SpriteImage_ControllerSwaying_Path,
    118: SpriteImage_ControllerSpinning_Path,
    183: SpriteImage_FallingIcicle,
    216: SpriteImage_BossController,
    245: SpriteImage_BossController,
    288: SpriteImage_Bush,
    301: SpriteImage_GiantWiggler,
    325: SpriteImage_DashCoin,
    359: SpriteImage_LavaBlock,
    412: SpriteImage_BossController,
    432: SpriteImage_BossController,
    435: SpriteImage_BossController,
    440: SpriteImage_Debris,
    450: SpriteImage_KamekBlock,
    466: SpriteImage_BossController,
    476: SpriteImage_GiantKoopaTroopa,
    497: SpriteImage_BossController,
    522: SpriteImage_FloatingBarrel,
    599: SpriteImage_GoalRing,
    366: SpriteImage_CoinSnake,
    391: SpriteImage_GrayCrystal,
    190: SpriteImage_PivotaBlock,
    191: SpriteImage_PivotaBrick,
    305: SpriteImage_Poltergeist,
    310: SpriteImage_Candlestick,
}
