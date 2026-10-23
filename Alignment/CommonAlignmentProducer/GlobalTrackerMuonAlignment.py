import FWCore.ParameterSet.Config as cms

def GlobalTrackerMuonAlignment(*args, **kwargs):
  mod = cms.EDAnalyzer('GlobalTrackerMuonAlignment',
    propagator = cms.string('SteppingHelixPropagator'),
    tracks = cms.InputTag('ALCARECOMuAlGlobalCosmics', 'TrackerOnly'),
    muons = cms.InputTag('ALCARECOMuAlGlobalCosmics', 'StandAlone'),
    gmuons = cms.InputTag('ALCARECOMuAlGlobalCosmics', 'GlobalMuon'),
    smuons = cms.InputTag('ALCARECOMuAlGlobalCosmics', 'SelectedMuons'),
    isolated = cms.bool(False),
    cosmics = cms.bool(False),
    refitmuon = cms.bool(False),
    refittrack = cms.bool(False),
    rootOutFile = cms.untracked.string('outfile.root'),
    txtOutFile = cms.untracked.string('outglobal.txt'),
    writeDB = cms.untracked.bool(False),
    debug = cms.untracked.bool(False),
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
