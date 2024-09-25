import FWCore.ParameterSet.Config as cms

def BunchSpacingProducer(*args, **kwargs):
  mod = cms.EDProducer('BunchSpacingProducer',
    overrideBunchSpacing = cms.bool(False),
    bunchSpacingOverride = cms.uint32(25),
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
