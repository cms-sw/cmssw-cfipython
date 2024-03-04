import FWCore.ParameterSet.Config as cms

def PFEGammaToCandidateRemapper(**kwargs):
  mod = cms.EDProducer('PFEGammaToCandidateRemapper',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
