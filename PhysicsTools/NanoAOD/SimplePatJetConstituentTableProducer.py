import FWCore.ParameterSet.Config as cms

def SimplePatJetConstituentTableProducer(**kwargs):
  mod = cms.EDProducer('SimplePatJetConstituentTableProducer',
    name = cms.string('FatJetPFCand'),
    candIdxName = cms.string('PFCandIdx'),
    candIdxDoc = cms.string('Index in PFCand table'),
    jets = cms.InputTag('finalJetsAK8'),
    candidates = cms.InputTag('packedPFCandidates'),
    jetCut = cms.string(''),
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
