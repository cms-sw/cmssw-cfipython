import FWCore.ParameterSet.Config as cms

cosmicSplitterValidation = cms.EDAnalyzer('CosmicSplitterValidation',
  compressionSettings = cms.untracked.int32(-1),
  splitTracks = cms.InputTag('FinalTrackRefitter', '', 'splitter'),
  splitGlobalMuons = cms.InputTag('muons', '', 'splitter'),
  originalTracks = cms.InputTag('FirstTrackRefitter', '', 'splitter'),
  originalGlobalMuons = cms.InputTag('muons', '', 'Rec'),
  checkIfGolden = cms.bool(False),
  ifSplitMuons = cms.bool(False),
  mightGet = cms.optional.untracked.vstring
)
