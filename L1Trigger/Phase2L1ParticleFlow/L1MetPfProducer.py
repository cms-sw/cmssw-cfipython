import FWCore.ParameterSet.Config as cms

def L1MetPfProducer(**kwargs):
  mod = cms.EDProducer('L1MetPfProducer',
    L1PFObjects = cms.InputTag('L1PFProducer', 'l1pfCandidates'),
    maxCands = cms.int32(128),
    modelVersion = cms.string(''),
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
