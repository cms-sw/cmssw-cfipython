import FWCore.ParameterSet.Config as cms

ppsAlignmentWorker = cms.EDProducer('PPSAlignmentWorker',
  label = cms.string(''),
  tracksTags = cms.VInputTag('ctppsLocalTrackLiteProducer'),
  dqm_dir = cms.string('AlCaReco/PPSAlignment'),
  debug = cms.bool(False),
  mightGet = cms.optional.untracked.vstring
)
