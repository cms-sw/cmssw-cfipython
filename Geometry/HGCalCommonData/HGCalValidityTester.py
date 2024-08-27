import FWCore.ParameterSet.Config as cms

def HGCalValidityTester(**kwargs):
  mod = cms.EDAnalyzer('HGCalValidityTester',
    nameDetectors = cms.vstring(
      'HGCalEESensitive',
      'HGCalHESiliconSensitive',
      'HGCalHEScintillatorSensitive'
    ),
    fileName = cms.string('missD88.txt'),
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
