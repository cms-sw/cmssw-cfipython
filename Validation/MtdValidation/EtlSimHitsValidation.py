import FWCore.ParameterSet.Config as cms

def EtlSimHitsValidation(**kwargs):
  mod = cms.EDProducer('EtlSimHitsValidation',
    folder = cms.string('MTD/ETL/SimHits'),
    inputTag = cms.InputTag('mix', 'g4SimHitsFastTimerHitsEndcap'),
    hitMinimumEnergy2Dis = cms.double(0.001),
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
