import FWCore.ParameterSet.Config as cms

hltFindMatchingECALDigisToRechits = cms.EDProducer('HLTRechitsToDigis',
  region = cms.string('barrel'),
  digisIn = cms.InputTag('ecalDigis', 'ebDigis'),
  digisOut = cms.string('pi0EBDigis'),
  recHits = cms.InputTag('hltAlCaPi0EBUncalibrator', 'pi0EcalRecHitsEB'),
  srFlagsIn = cms.InputTag(''),
  srFlagsOut = cms.string('pi0EBSrFlags'),
  mightGet = cms.optional.untracked.vstring
)
