import FWCore.ParameterSet.Config as cms

def L2TauJetsMerger(**kwargs):
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
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
