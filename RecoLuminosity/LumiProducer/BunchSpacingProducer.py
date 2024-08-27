import FWCore.ParameterSet.Config as cms

def BunchSpacingProducer(**kwargs):
  mod = cms.EDProducer('BunchSpacingProducer',
    overrideBunchSpacing = cms.bool(False),
    bunchSpacingOverride = cms.uint32(25),
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
