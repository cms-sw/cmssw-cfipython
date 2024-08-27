import FWCore.ParameterSet.Config as cms

def MuonFSRAssociator(**kwargs):
  mod = cms.EDProducer('MuonFSRAssociator',
    photons = cms.required.InputTag,
    muons = cms.required.InputTag,
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
