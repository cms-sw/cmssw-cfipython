import FWCore.ParameterSet.Config as cms

tkAlCaOverlapTagger = cms.EDProducer('TkAlCaOverlapTagger',
  src = cms.InputTag('generalTracks'),
  Clustersrc = cms.InputTag('ALCARECOTkAlCosmicsCTF0T'),
  rejectBadMods = cms.bool(False),
  BadMods = cms.vuint32(),
  mightGet = cms.optional.untracked.vstring
)
