import FWCore.ParameterSet.Config as cms

def MkFitSeedConverter(*args, **kwargs):
  mod = cms.EDProducer('MkFitSeedConverter',
    seeds = cms.InputTag('initialStepSeeds'),
    ttrhBuilder = cms.ESInputTag('', 'WithTrackAngle'),
    maxNSeeds = cms.uint32(500000),
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
