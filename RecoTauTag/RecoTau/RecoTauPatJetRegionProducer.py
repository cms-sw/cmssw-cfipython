import FWCore.ParameterSet.Config as cms

def RecoTauPatJetRegionProducer(*args, **kwargs):
  mod = cms.EDProducer('RecoTauPatJetRegionProducer',
    src = cms.InputTag('ak4PFJets'),
    deltaR = cms.double(0.8),
    pfCandAssocMapSrc = cms.InputTag(''),
    verbosity = cms.int32(0),
    maxJetAbsEta = cms.double(2.5),
    minJetPt = cms.double(14),
    pfCandSrc = cms.InputTag('particleFlow'),
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
