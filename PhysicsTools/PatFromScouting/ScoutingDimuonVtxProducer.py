import FWCore.ParameterSet.Config as cms

def ScoutingDimuonVtxProducer(*args, **kwargs):
  mod = cms.EDProducer('ScoutingDimuonVtxProducer',
    scoutingMuons = cms.InputTag('hltScoutingMuonPackerVtx'),
    scoutingVertices = cms.InputTag('hltScoutingMuonPackerVtx', 'displacedVtx'),
    patMuons = cms.InputTag('slimmedMuons'),
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
