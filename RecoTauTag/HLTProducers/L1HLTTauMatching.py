import FWCore.ParameterSet.Config as cms

def L1HLTTauMatching(**kwargs):
  mod = cms.EDProducer('L1HLTTauMatching',
    L1TauTrigger = cms.InputTag('hltL1sDoubleIsoTau40er'),
    JetSrc = cms.InputTag('hltSelectedPFTausTrackPt1MediumIsolationReg'),
    EtMin = cms.double(0),
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
