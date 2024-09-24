import FWCore.ParameterSet.Config as cms

def SimpleGenJetConstituentTableProducer(*args, **kwargs):
  mod = cms.EDProducer('SimpleGenJetConstituentTableProducer',
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
