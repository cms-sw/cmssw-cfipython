import FWCore.ParameterSet.Config as cms

def MkFitSeedConverter(**kwargs):
  mod = cms.EDProducer('MkFitSeedConverter',
    seeds = cms.InputTag('initialStepSeeds'),
    ttrhBuilder = cms.ESInputTag('', 'WithTrackAngle'),
    maxNSeeds = cms.uint32(500000),
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
