import FWCore.ParameterSet.Config as cms

def MuonFSRAssociator(*args, **kwargs):
  mod = cms.EDProducer('MuonFSRAssociator',
    photons = cms.required.InputTag,
    muons = cms.required.InputTag,
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
