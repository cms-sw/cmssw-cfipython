import FWCore.ParameterSet.Config as cms

def SimplePatJetConstituentTableProducer(*args, **kwargs):
  mod = cms.EDProducer('SimplePatJetConstituentTableProducer',
    name = cms.string('FatJetPFCand'),
    candIdxName = cms.string('PFCandIdx'),
    candIdxDoc = cms.string('Index in PFCand table'),
    jets = cms.InputTag('finalJetsAK8'),
    candidates = cms.InputTag('packedPFCandidates'),
    jetCut = cms.string(''),
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
