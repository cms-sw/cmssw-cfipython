import FWCore.ParameterSet.Config as cms

def CosmicSplitterValidation(**kwargs):
  mod = cms.EDAnalyzer('CosmicSplitterValidation',
    compressionSettings = cms.untracked.int32(-1),
    splitTracks = cms.InputTag('FinalTrackRefitter', '', 'splitter'),
    splitGlobalMuons = cms.InputTag('muons', '', 'splitter'),
    originalTracks = cms.InputTag('FirstTrackRefitter', '', 'splitter'),
    originalGlobalMuons = cms.InputTag('muons', '', 'Rec'),
    checkIfGolden = cms.bool(False),
    ifSplitMuons = cms.bool(False),
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
