import FWCore.ParameterSet.Config as cms

def SoftPFMuonTagInfoProducer(**kwargs):
  mod = cms.EDProducer('SoftPFMuonTagInfoProducer',
    jets = cms.required.InputTag,
    muons = cms.required.InputTag,
    primaryVertex = cms.required.InputTag,
    muonPt = cms.required.double,
    muonSIPsig = cms.required.double,
    filterIpsig = cms.required.double,
    filterRatio1 = cms.required.double,
    filterRatio2 = cms.required.double,
    filterPromptMuons = cms.required.bool,
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
