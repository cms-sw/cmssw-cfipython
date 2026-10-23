import FWCore.ParameterSet.Config as cms

def CaloJetBxSelector(*args, **kwargs):
  mod = cms.EDProducer('CaloJetBxSelector',
    jetsTag = cms.required.InputTag,
    minNJet = cms.uint32(0),
    minJetPt = cms.vdouble(),
    maxJetAbsEta = cms.vdouble(),
    minJetNConst = cms.vint32(),
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
