import FWCore.ParameterSet.Config as cms

def MEtoEDMConverter(**kwargs):
  mod = cms.EDProducer('MEtoEDMConverter',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
