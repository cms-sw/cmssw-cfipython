import FWCore.ParameterSet.Config as cms

def ScoutingCollectionMonitor(*args, **kwargs):
  mod = cms.EDProducer('ScoutingCollectionMonitor',
    OutputInternalPath = cms.string('MY_FOLDER'),
    triggerresults = cms.InputTag('TriggerResults', '', 'HLT'),
    electrons = cms.InputTag('hltScoutingEgammaPacker'),
    muons = cms.InputTag('hltScoutingMuonPackerNoVtx'),
    pfcands = cms.InputTag('hltScoutingPFPacker'),
    photons = cms.InputTag('hltScoutingEgammaPacker'),
    pfjets = cms.InputTag('hltScoutingPFPacker'),
    tracks = cms.InputTag('hltScoutingTrackPacker'),
    displacedVertices = cms.InputTag('hltScoutingMuonPackerNoVtx', 'displacedVtx'),
    primaryVertices = cms.InputTag('hltScoutingPrimaryVertexPacker', 'primaryVtx'),
    pfMetPt = cms.InputTag('hltScoutingPFPacker', 'pfMetPt'),
    pfMetPhi = cms.InputTag('hltScoutingPFPacker', 'pfMetPhi'),
    rho = cms.InputTag('hltScoutingPFPacker', 'rho'),
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
