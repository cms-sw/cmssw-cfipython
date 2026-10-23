import FWCore.ParameterSet.Config as cms

def ScoutingMuonTagProbeAnalyzer(*args, **kwargs):
  mod = cms.EDProducer('ScoutingMuonTagProbeAnalyzer',
    OutputInternalPath = cms.string('MY_FOLDER'),
    ScoutingMuonCollection = cms.InputTag('Run3ScoutingMuons'),
    ScoutingVtxCollection = cms.InputTag('hltScoutingMuonPackerNoVtx'),
    runWithoutVertex = cms.bool(True),
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
