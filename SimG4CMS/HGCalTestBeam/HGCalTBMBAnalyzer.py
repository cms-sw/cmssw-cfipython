import FWCore.ParameterSet.Config as cms

def HGCalTBMBAnalyzer(**kwargs):
  mod = cms.EDAnalyzer('HGCalTBMBAnalyzer',
    detectorNames = cms.vstring(
      'HGCalBeamWChamb',
      'HGCalBeamS1',
      'HGCalBeamS2',
      'HGCalBeamS3',
      'HGCalBeamS4',
      'HGCalBeamS5',
      'HGCalBeamS6',
      'HGCalBeamCK3',
      'HGCalBeamHaloCounter',
      'HGCalBeamMuonCounter',
      'HGCalEE',
      'HGCalHE',
      'HGCalAH'
    ),
    labelMBCalo = cms.InputTag('g4SimHits', 'HGCalTBMB'),
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
