import FWCore.ParameterSet.Config as cms

def LXXXCorrectorProducer(**kwargs):
  mod = cms.EDProducer('LXXXCorrectorProducer',
    level = cms.required.string,
    algorithm = cms.required.string,
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
