import FWCore.ParameterSet.Config as cms

def MuDTTPGThetaFlatTableProducer(*args, **kwargs):
  mod = cms.EDProducer('MuDTTPGThetaFlatTableProducer',
    name = cms.string('ltBmtfInTh'),
    tag = cms.string('BMTF_IN'),
    src = cms.InputTag('bmtfDigis'),
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
