import FWCore.ParameterSet.Config as cms

pfCandidateRecalibrator = cms.EDProducer('PFCandidateRecalibrator',
  pfcandidates = cms.InputTag('particleFlow'),
  shortFibreThr = cms.double(1.4),
  longFibreThr = cms.double(1.4)
)
