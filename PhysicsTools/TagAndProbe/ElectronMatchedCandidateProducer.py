import FWCore.ParameterSet.Config as cms

def ElectronMatchedCandidateProducer(**kwargs):
  mod = cms.EDProducer('ElectronMatchedCandidateProducer',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
