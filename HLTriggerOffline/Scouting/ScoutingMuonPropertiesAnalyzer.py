import FWCore.ParameterSet.Config as cms

def ScoutingMuonPropertiesAnalyzer(*args, **kwargs):
  mod = cms.EDProducer('ScoutingMuonPropertiesAnalyzer',
    OutputInternalPath = cms.string('HLT/ScoutingOffline/Muons/Properties'),
    fillAllHistograms = cms.bool(False),
    triggerResults = cms.InputTag('TriggerResults', '', 'HLT'),
    muonsNoVtx = cms.InputTag('hltScoutingMuonPackerNoVtx'),
    muonsVtx = cms.InputTag('hltScoutingMuonPackerVtx'),
    PV = cms.InputTag('hltScoutingPrimaryVertexPacker', 'primaryVtx'),
    SVNoVtx = cms.InputTag('hltScoutingMuonPackerNoVtx', 'displacedVtx'),
    SVVtx = cms.InputTag('hltScoutingMuonPackerVtx', 'displacedVtx'),
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
