import FWCore.ParameterSet.Config as cms

def BtlSimHitsValidation(**kwargs):
  mod = cms.EDProducer('BtlSimHitsValidation',
    folder = cms.string('MTD/BTL/SimHits'),
    inputTag = cms.InputTag('mix', 'g4SimHitsFastTimerHitsBarrel'),
    hitMinimumEnergy = cms.double(1),
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
