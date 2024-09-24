import FWCore.ParameterSet.Config as cms

def L1HLTTauMatching(*args, **kwargs):
  mod = cms.EDProducer('L1HLTTauMatching',
    L1TauTrigger = cms.InputTag('hltL1sDoubleIsoTau40er'),
    JetSrc = cms.InputTag('hltSelectedPFTausTrackPt1MediumIsolationReg'),
    EtMin = cms.double(0),
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
