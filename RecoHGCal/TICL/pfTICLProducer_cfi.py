import FWCore.ParameterSet.Config as cms

pfTICLProducer = cms.EDProducer('PFTICLProducer',
  ticlCandidateSrc = cms.InputTag('ticlTrackstersMerge'),
  trackTimeValueMap = cms.InputTag('tofPID', 't0'),
  trackTimeErrorMap = cms.InputTag('tofPID', 'sigmat0'),
  trackTimeQualityMap = cms.InputTag('mtdTrackQualityMVA', 'mtdQualMVA'),
  timingQualityThreshold = cms.double(0.5),
  useTimingAverage = cms.bool(False),
  mightGet = cms.optional.untracked.vstring
)
