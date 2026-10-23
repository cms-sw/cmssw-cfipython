import FWCore.ParameterSet.Config as cms

def PatFromScoutingJetProducer(*args, **kwargs):
  mod = cms.EDProducer('PatFromScoutingJetProducer',
    src = cms.InputTag('hltScoutingPFPacker'),
    pfCandidates = cms.InputTag('packedPFCandidates'),
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
