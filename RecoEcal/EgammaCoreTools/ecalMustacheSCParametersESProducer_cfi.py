import FWCore.ParameterSet.Config as cms

ecalMustacheSCParametersESProducer = cms.ESProducer('EcalMustacheSCParametersESProducer',
  sqrtLogClustETuning = cms.double(1.1),
  parabolaParameterSets = cms.VPSet(
    cms.PSet(
      etaMin = cms.double(0),
      log10EMin = cms.double(-3),
      pLow = cms.vdouble(
        -0.0268843,
        0.147742,
        -0.0191235
      ),
      pUp = cms.vdouble(
        -0.107537,
        0.590969,
        -0.076494
      ),
      w0Low = cms.vdouble(
        -0.00681785,
        -0.00239516
      ),
      w0Up = cms.vdouble(
        -0.00681785,
        -0.00239516
      ),
      w1Low = cms.vdouble(
        0.000699995,
        -0.00554331
      ),
      w1Up = cms.vdouble(
        0.000699995,
        -0.00554331
      )
    )
  ),
  appendToDataLabel = cms.string('')
)
