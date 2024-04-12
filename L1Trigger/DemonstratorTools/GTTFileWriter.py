import FWCore.ParameterSet.Config as cms

def GTTFileWriter(**kwargs):
  mod = cms.EDAnalyzer('GTTFileWriter',
    tracks = cms.untracked.InputTag('l1tTTTracksFromTrackletEmulation', 'Level1TTTracks'),
    convertedTracks = cms.untracked.InputTag('l1tGTTInputProducer', 'Level1TTTracksConverted'),
    selectedTracks = cms.untracked.InputTag('l1tTrackSelectionProducer', 'Level1TTTracksSelectedEmulation'),
    vertexAssociatedTracks = cms.untracked.InputTag('l1tTrackSelectionProducer', 'Level1TTTracksSelectedAssociatedEmulation'),
    vertices = cms.untracked.InputTag('l1tVertexProducer', 'L1VerticesEmulation'),
    jets = cms.untracked.InputTag('l1tTrackJetsEmulation', 'L1TrackJets'),
    htmiss = cms.untracked.InputTag('l1tTrackerEmuHTMiss', 'L1TrackerEmuHTMiss'),
    htmissdisp = cms.untracked.InputTag('l1tTrackerEmuHTMissExtended', 'L1TrackerEmuHTMissExtended'),
    etmiss = cms.untracked.InputTag('l1tTrackerEmuEtMiss', 'L1TrackerEmuEtMiss'),
    inputFilename = cms.untracked.string('L1GTTInputFile'),
    inputConvertedFilename = cms.untracked.string('L1GTTInputConvertedFile'),
    selectedTracksFilename = cms.untracked.string('L1GTTSelectedTracksFile'),
    vertexAssociatedTracksFilename = cms.untracked.string('L1GTTVertexAssociatedTracksFile'),
    outputCorrelatorFilename = cms.untracked.string('L1GTTOutputToCorrelatorFile'),
    outputGlobalTriggerFilename = cms.untracked.string('L1GTTOutputToGlobalTriggerFile'),
    format = cms.untracked.string('APx'),
    fileExtension = cms.untracked.string('txt'),
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
