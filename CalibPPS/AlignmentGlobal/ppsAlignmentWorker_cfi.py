import FWCore.ParameterSet.Config as cms

ppsAlignmentWorker = cms.EDProducer('PPSAlignmentWorker',
  label = cms.string(''),
  tagTracks = cms.InputTag('ctppsLocalTrackLiteProducer'),
  folder = cms.string('AlCaReco/PPSAlignment'),
  debug = cms.bool(False),
  mightGet = cms.optional.untracked.vstring
)
