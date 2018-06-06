import FWCore.ParameterSet.Config as cms

hcalRecAlgos = cms.ESProducer('HcalRecAlgoESProducer',
  phase = cms.uint32(0),
  RecoveredRecHitBits = cms.vstring(
    'TimingAddedBit',
    'TimingSubtractedBit'
  ),
  SeverityLevels = cms.VPSet(
    cms.PSet(
      ChannelStatus = cms.vstring(''),
      Level = cms.int32(0),
      RecHitFlags = cms.vstring('')
    ),
    cms.PSet(
      ChannelStatus = cms.vstring('HcalCellCaloTowerProb'),
      Level = cms.int32(1),
      RecHitFlags = cms.vstring('')
    ),
    cms.PSet(
      ChannelStatus = cms.vstring('HcalCellExcludeFromHBHENoiseSummary'),
      Level = cms.int32(5),
      RecHitFlags = cms.vstring(
        'HSCP_R1R2',
        'HSCP_FracLeader',
        'HSCP_OuterEnergy',
        'HSCP_ExpFit',
        'ADCSaturationBit',
        'HBHEIsolatedNoise',
        'AddedSimHcalNoise'
      )
    ),
    cms.PSet(
      ChannelStatus = cms.vstring(''),
      Level = cms.int32(8),
      RecHitFlags = cms.vstring(
        'HBHEHpdHitMultiplicity',
        'HBHEPulseShape',
        'HOBit',
        'HFDigiTime',
        'HFInTimeWindow',
        'ZDCBit',
        'CalibrationBit',
        'TimingErrorBit',
        'HBHEFlatNoise',
        'HBHESpikeNoise',
        'HBHETriangleNoise',
        'HBHETS4TS5Noise',
        'HBHENegativeNoise',
        'HBHEOOTPU'
      )
    ),
    cms.PSet(
      ChannelStatus = cms.vstring(''),
      Level = cms.int32(11),
      RecHitFlags = cms.vstring(
        'HFLongShort',
        'HFPET',
        'HFS8S1Ratio'
      )
    ),
    cms.PSet(
      ChannelStatus = cms.vstring('HcalCellCaloTowerMask'),
      Level = cms.int32(12),
      RecHitFlags = cms.vstring('')
    ),
    cms.PSet(
      ChannelStatus = cms.vstring('HcalCellHot'),
      Level = cms.int32(15),
      RecHitFlags = cms.vstring('')
    ),
    cms.PSet(
      ChannelStatus = cms.vstring(
        'HcalCellOff',
        'HcalCellDead'
      ),
      Level = cms.int32(20),
      RecHitFlags = cms.vstring('')
    )
  ),
  DropChannelStatusBits = cms.vstring(
    'HcalCellMask',
    'HcalCellOff',
    'HcalCellDead'
  ),
  appendToDataLabel = cms.string('')
)
