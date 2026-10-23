import FWCore.ParameterSet.Config as cms

def MuonVertexTableProducer(*args, **kwargs):
  mod = cms.EDProducer('MuonVertexTableProducer',
    patMuons = cms.required.InputTag,
    dsaMuons = cms.required.InputTag,
    beamspot = cms.required.InputTag,
    primaryVertex = cms.required.InputTag,
    generalTracks = cms.required.InputTag,
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
