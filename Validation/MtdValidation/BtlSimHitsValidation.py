import FWCore.ParameterSet.Config as cms

def BtlSimHitsValidation(*args, **kwargs):
  mod = cms.EDProducer('BtlSimHitsValidation',
    folder = cms.string('MTD/BTL/SimHits'),
    inputTag = cms.InputTag('mix', 'g4SimHitsFastTimerHitsBarrel'),
    hitMinimumEnergy = cms.double(1),
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
