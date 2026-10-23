import FWCore.ParameterSet.Config as cms

def HGCalTBMBAnalyzer(*args, **kwargs):
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
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
