import FWCore.ParameterSet.Config as cms

patTauSignalCandidatesProducer = cms.EDProducer('PATTauSignalCandidatesProducer',
  src = cms.InputTag('slimmedTaus'),
  storeLostTracks = cms.bool(True),
  mightGet = cms.optional.untracked.vstring
)
