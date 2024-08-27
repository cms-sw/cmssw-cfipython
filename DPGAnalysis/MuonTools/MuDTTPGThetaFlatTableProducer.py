import FWCore.ParameterSet.Config as cms

def MuDTTPGThetaFlatTableProducer(**kwargs):
  mod = cms.EDProducer('MuDTTPGThetaFlatTableProducer',
    name = cms.string('ltBmtfInTh'),
    tag = cms.string('BMTF_IN'),
    src = cms.InputTag('bmtfDigis'),
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
