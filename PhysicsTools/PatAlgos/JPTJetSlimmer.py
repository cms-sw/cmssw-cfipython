import FWCore.ParameterSet.Config as cms

def JPTJetSlimmer(**kwargs):
  mod = cms.EDProducer('JPTJetSlimmer',
    src = cms.InputTag('JetPlusTrackZSPCorJetAntiKt4'),
    srcCalo = cms.InputTag('slimmedCaloJets'),
    cut = cms.string('pt>20'),
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
