import FWCore.ParameterSet.Config as cms

def HiggsDQM(**kwargs):
  mod = cms.EDProducer('HiggsDQM',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
