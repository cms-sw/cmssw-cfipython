import FWCore.ParameterSet.Config as cms

def MuDTTPGPhiFlatTableProducer(**kwargs):
  mod = cms.EDProducer('MuDTTPGPhiFlatTableProducer',
    name = cms.string('ltBmtfIn'),
    tag = cms.string('BMTF_IN'),
    src = cms.InputTag('bmtfDigis'),
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
