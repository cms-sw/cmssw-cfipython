import FWCore.ParameterSet.Config as cms

def JPTJetSlimmer(*args, **kwargs):
  mod = cms.EDProducer('JPTJetSlimmer',
    src = cms.InputTag('JetPlusTrackZSPCorJetAntiKt4'),
    srcCalo = cms.InputTag('slimmedCaloJets'),
    cut = cms.string('pt>20'),
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
