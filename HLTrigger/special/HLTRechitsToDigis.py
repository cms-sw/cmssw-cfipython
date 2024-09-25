import FWCore.ParameterSet.Config as cms

def HLTRechitsToDigis(*args, **kwargs):
  mod = cms.EDProducer('HLTRechitsToDigis',
    region = cms.string('barrel'),
    digisIn = cms.InputTag('ecalDigis', 'ebDigis'),
    digisOut = cms.string('pi0EBDigis'),
    recHits = cms.InputTag('hltAlCaPi0EBUncalibrator', 'pi0EcalRecHitsEB'),
    srFlagsIn = cms.InputTag(''),
    srFlagsOut = cms.string('pi0EBSrFlags'),
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
