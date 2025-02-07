import FWCore.ParameterSet.Config as cms

def L2TauJetsMerger(*args, **kwargs):
  mod = cms.EDProducer('L2TauJetsMerger',
    JetSrc = cms.VInputTag(
      'hltAkIsoTau1Regional',
      'hltAkIsoTau2Regional',
      'hltAkIsoTau3Regional',
      'hltAkIsoTau4Regional'
    ),
    EtMin = cms.double(20),
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
